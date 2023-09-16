FROM python:3.9-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /core

# commands for reqs.txt
RUN pip3 install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy entire project into new WORKDIR /core
COPY . .

# run server
CMD python manage.py runserver 0.0.0.0:8000