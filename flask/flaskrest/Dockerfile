FROM ubuntu:20.04

RUN mkdir /flaskrest
COPY . /flaskrest/

WORKDIR /flaskrest

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y python3.8 python3-pip default-libmysqlclient-dev
RUN pip3 install -r requirements.txt

CMD uwsgi uwsgi.ini