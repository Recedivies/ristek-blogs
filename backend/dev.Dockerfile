# pull the official docker image
FROM python:3.9.6-alpine

# set work directory
WORKDIR /usr/src/app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .

RUN  \
    apk update && \
    apk upgrade && \
    apk add --no-cache bash && \
    apk add --no-cache --virtual .build-deps gcc musl-dev && \
    pip3 install --upgrade pip -r requirements.txt && \
    apk --purge del .build-deps

# copy project
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]