FROM python:3.9.6-alpine

RUN mkdir -p /home/upload-api

ENV HOME=/home/upload-api
ENV APP_HOME=/home/upload-api/api

RUN mkdir ${APP_HOME}
RUN mkdir ${APP_HOME}/staticfiles
RUN mkdir ${APP_HOME}/uploads


WORKDIR ${APP_HOME}

# python buffer & bytecode exception
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# db dependecies
RUN apk update \
    && apk add g++ postgresql-dev gcc python3-dev musl-dev

# install packages
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /home/upload-api/api/entrypoint.sh
RUN chmod +x /home/upload-api/api/entrypoint.sh

# copy project to container
COPY . ${APP_HOME}