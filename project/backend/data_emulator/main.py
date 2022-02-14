from random import randrange, randint
from faker import Faker
import schedule
import time
from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import func
import pandas as pd

meta = MetaData()


def connect(db_uri):
    engine = create_engine(db_uri)
    return engine.connect()


def purchases(args):
    rng = args[0]  # Get numeric value from scheduler
    db = args[1]  # Get DB url connection
    loops = randrange(1, rng)  # Generate a dynamic number of users to create
    conn = connect(db_uri=db)  # Instantiate the DB connection
    fake = Faker()  # Instantiate Faker
    usr_bcs = []  # Instantiate array for batch users insert purpose
    prc_bcs = []  # Instantiate array for batch purchases insert purpose
    for i in range(loops):
        # Insert individual records in real-time
        username = fake.user_name()  # Generate fake username
        dt = str(func.now())  # Set the current timestamp
        # Instantiate the user object
        usr = {"username": username, "name": fake.name(), "job": fake.job(), "email": fake.email(),
               "address": fake.address(), "phone": fake.phone_number(), "datetime": dt}
        # Create a DF in order to make it easy to insert into the DB
        user_df = pd.DataFrame.from_records([usr])
        # Append record to the DB
        user_df.to_sql('users', con=conn, if_exists="append", index=False)
        # Add record to the batch array
        usr_bcs.append(usr)
        prs = {"username": username, "country": fake.country(), "latitude": str(fake.latitude()),
               "longitude": str(fake.longitude()), "currency": str(fake.currency()),
               "ipv4": fake.ipv4(), "user_agent": fake.user_agent(),
               "cc_expire": fake.credit_card_expire(), "cc_number": fake.credit_card_number(),
               "cc_provider": fake.credit_card_provider(), "cc_sec_code": fake.credit_card_security_code(),
               "datetime": dt}
        # Create a DF in order to make it easy to insert into the DB
        purchase_df = pd.DataFrame.from_records([prs])
        # Append record to the DB
        purchase_df.to_sql('purchases', con=conn, if_exists="append", index=False)
        # Add record to the batch array
        prc_bcs.append(prs)

    # Insert batch transactions - Near Real Time
    user_batches = pd.DataFrame.from_records(usr_bcs)
    user_batches.to_sql('users', con=conn, if_exists="append", index=False)
    prchs_batches = pd.DataFrame.from_records(prc_bcs)
    prchs_batches.to_sql('purchases', con=conn, if_exists="append", index=False)

    # Track batch of fake records generated, this won't match the actual inserts (by design we only focus
    # on the fake records created, not the number of instances inserted/appended to the DB)
    dt = str(func.now())
    track_row = {"records": loops, "datetime": dt}
    track_df = pd.DataFrame.from_records([track_row])
    track_df.to_sql('track', con=conn, if_exists="append", index=False)

    conn.close()  # Close DB connection


if __name__ == '__main__':
    db_uri = "cockroachdb://root@192.168.86.214:26257/defaultdb?sslmode=disable"

    # Submit load test every 1 min: with a range of users from/up-to 1-50 where a=50 and 1 is hardcoded by default
    schedule.every(1).minutes.do(purchases, args=[1000, db_uri])
    schedule.every(5).minutes.do(purchases, args=[1000, db_uri])
    schedule.every(5).minutes.do(purchases, args=[10000, db_uri])
    # Submit load test every hour: with a range of users from/up-to 1-500 where a=500 and 1 is hardcoded by default
    #schedule.every().hour.do(purchases, args=[1000, db_uri])
    # Submit load test every saturday: with a range of users from/up-to 1-5000 where a=500 and 1 is hardcoded by default
    #schedule.every().saturday.do(purchases, args=[10000, db_uri])
    while True:
        # Checks whether a scheduled task
        # is pending to run or not
        schedule.run_pending()
        time.sleep(1)
