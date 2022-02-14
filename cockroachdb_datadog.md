# CockroackDB + Datadog

According to the [`Cost of a Data Breach - A view from the cloud 2021` report](https://www.ibm.com/downloads/cas/JDALZGKJ), the average cost of hybrid and/or cloud security breached is to be $4.80 Million USD. The type of damage caused by a single security breach affects applications, network, servers, and the most important gold mine of every company: it's data storage. [Unitrends - What Are the Consequences of Data Loss? by Mark Campbell](https://www.unitrends.com/blog/what-are-the-consequences-of-data-loss) also has a breakdown of the risks and consequences of data loss, such as 93% filling for bankruptcy when data loss for over 10 days, that stems from multiple reasons. 

The risk of never reopening for business or paying high costs data recovery, is greater due to security threats or improperly (or not) monitored technology ecosystem.

## Objective

---

Through the following project focuses on two important aspects of the technology stack of companies, whether they are located on premise, cloud, or have a hybrid architecture. In the current project, we will focus on Cockroach DB scalability and the ability of Datadog to monitor the database for a full observability. The primary goal of the following writing is to highlight the advantages of each technology and not to discuss the comparison to other similar products or competitors; therefore we will not discuss what other competitors perceive as detractors for CockroachDB & Datadog.

### Why CockroachDB?

The name of the company and or product in itself is a head turning marketing strategy. Our common perception of cockroaches is that they can survive a nuclear blast and never die. Cockroach labs applies the same concept for the survival of the OLTP transactional data storage of every business: the database. For the readers who are familiar with the Hadoop distributed data computation, Cockroach Labs applies the evolution of distributed data with the Cockroach Database to ensure optimal availability, resiliency, and distributed data across geo-locations. 

**The Why: [Never worry about your database again](https://www.cockroachlabs.com/)**

* Resilience
* Distributed
* Quick time to deploy
* High Availability
* Omni-presence: Cloud (VMs, Functions, Managed), On-Prem, Hybrid
* Scalability
* [Transparent pricing & tiers](https://www.cockroachlabs.com/pricing/)
* more

### Why Datadog?

Having gone through the ringer, a common expression of rough/difficult experiences, with on-call duties, application development, database process redesign, overall systems monitoring, and endless 3 am false alert pager calls, I was able to understand how the criticality of seeing data in a single place for better decision making. 
Datadog's main concept is unification of monitored data to present an observability solution. More than just a single point solution, it uses one agent to turn on multiple monitoring tools (Network, Host Metrics, Live Process inventory, Log management, deep Database monitoring, security, and many more) and completes the full circle with over 500+ integrations and Cloud crawler integrations.

**The Why: [Modern monitoring & Security](https://www.datadoghq.com/)**

* One agent install with multiple tools
  * CPU usage < 1% overall
  * eBPF event monitoring
  * Auto tagging
  * Multiple integrations (DBs, Big Data, JMX, and many more)
* SaaS platform
  * Every product is built from the ground up, rather than presenting siloed tools
* Robust rules, pipelines, offers
* ML + Watchdog
* Monitoring Out-of-the-box
* Out of the box Dashboards for most integrations
* Tag correlation
* [Transparent pricing & tiers](https://www.datadoghq.com/pricing/)
* more

## Project Integration Demo

To test the database cluster, we will use scripted data load, a Django interface, and Postman to make the API calls. Tools used in this project:

* [PyCharm CE](https://www.jetbrains.com/pycharm/download/)
* Git
* Python modules: random, [`Faker`](https://faker.readthedocs.io/en/master/), schedule, time, [`sqlalchemy`](https://pypi.org/project/SQLAlchemy/), [`pandas`](https://pypi.org/project/pandas/), Django, [`ddtrace`](https://pypi.org/project/ddtrace/), [`django-cockroachdb`](https://pypi.org/project/django-cockroachdb/), [`django-cors-headers`](https://pypi.org/project/django-cors-headers/), djangorestframework, psycopg2, psycopg2-binary, [`dj-database-url`](https://pypi.org/project/dj-database-url/)
* Docker, Docker Compose
* Remote VM to run CockroachDB cluster
* [Northwind](https://github.com/pthom/northwind_psql) SQL data set only for Django makemigrations.
* [Django Builder](https://djangobuilder.io/#/), to import the modules.py and generate the View and forms.
* [Postman Collection Runner](https://learning.postman.com/docs/running-collections/intro-to-collection-runs/)
* CockroachDB Docker Image
* Datadog Docker Image `datadog/agent`
* Datadog APM Python Library: [`ddtrace`](https://pypi.org/project/ddtrace/)

> Python packages

```commandline
pip install ddtrace dj-database-url \
Django \
django-cockroachdb \
django-cors-headers \
djangorestframework \
Faker \
psycopg2 \
psycopg2-binary \
requests \
schedule \
SQLAlchemy \
sqlalchemy-cockroachdb
```

The different databse package libraries are used for Django, Python, and SQL Alchemy. Django is not fully compatible with CockroachDB and the additional [`django-cockroachdb`](https://pypi.org/project/django-cockroachdb/) module is required.

**NOTE**: Whenever we see the Datadog flamegraphs, it will show two instances of a DB connection, which reflects the PostgreSQL driver and CockroachDB driver.

### Database load script

Before getting started with stress testing of the CockroachDB cluster, we will use the following Python script that emits fake requests to insert new users into the database. Here is the breakdown of what the script accomplishes:

* Random generate users based on the `Faker` Python module package, which provides random user data such as:
```python
>> faker.user_name(), faker.user_agent()
('rubengordon', 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/532.2 (KHTML, like Gecko) FxiOS/15.1j8991.0 Mobile/45C281 Safari/532.2')
```
* With the Schedule module, we assign a random insertion database load range of 1-10K records every minute in our Python [`main`]("project/backend/data_emulator/main.py") function:
```python
if __name__ == '__main__':
    db_uri = "cockroachdb://root@192.168.86.214:26257/defaultdb?sslmode=disable"

    # Submit load test every 1 min: with a range of users from/up-to 1-50 where a=50 and 1 is hardcoded by default
    schedule.every(1).minutes.do(purchases, args=[10000, db_uri])
```

### Frontend: Northwind Django app

```commandline
(venv) jlhernandez $ python manage.py runserver 0:3000
```

![Northwind Django]('images/northwind-django.png')

### Cockroach Labs Database Test

To test the capabilities of CockroachDB, there are a few samples provided by Cockroach Labs on how to do a quick start, such as the in-memory database cluster, Kubernetes Helm chart, Docker container, and self-managed installations.

For our demo purposes, I have configured the following docker-compose.yaml file to test the `Elastic Scale` of the architecture. To get started, lets breakdown our approach:

> Spin up a small CockroachDB cluster
> Apply database load
> Scale up the CockroachDB cluster
> Scale down the CockroachDB cluster

### Datadog Monitoring Test



## Sources:

* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
