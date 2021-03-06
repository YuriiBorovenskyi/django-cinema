# pull base image
FROM python:3.8
# set work directory
WORKDIR /usr/src/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apt-get update -y && apt-get install -y netcat gcc python3-dev musl-dev
RUN pip install --upgrade pip
# copy project
COPY . .
# install dependencies
RUN pip install -r requirements/dev.txt -r requirements/test.txt
