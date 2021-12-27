FROM python:3.8.10-slim-buster

ENV PYTHONUNBUFFERED=1
ENV APP_HOME=/app

RUN mkdir $APP_HOME
COPY ./requirements.txt $APP_HOME/
WORKDIR $APP_HOME

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends cron && rm -rf /var/lib/apt/lists/*

COPY ./source/ $APP_HOME/
