FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# We turn off the runserve below in order to control it with docker-compose.yaml, feel free to enable it if you
# just need the working image container
# ddtrace-run python manage.py runserver 0:3080
# CMD [ "ddtrace-run","python", "manage.py","runserver","--port=3000"]