# pull the official docker image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# Install Python dependencies
COPY ./backend/requirements.txt .
RUN pip3 install --upgrade pip -r requirements.txt
