FROM python:3.6.0

ADD requirements.txt /app/requirements.txt

WORKDIR /app/

RUN pip install -r requirements.txt

RUN adduser --disabled-password --gecos '' myuser
