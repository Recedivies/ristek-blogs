# Ristek Web Development Task

<div align="center" style="padding-bottom: 20px">
    <h1>Django + React + Docker + Heroku</h1>
    <img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" alt=""/>
    <img src="https://img.shields.io/badge/Docker-008FCC?style=for-the-badge&logo=docker&logoColor=white" alt=""/>
    <img src="https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white" alt=""/>
</div>

## Description:

A Profile Website which contains personal information and blogs with CRUD operations.

## Tools, libraries, frameworks:

### Backend

- `Python 3.8/9`
- `django` `djangorestframework` - Django + Django Rest Framework
- `django-cors-headers` - handling cross origin requests
- `gunicorn` - production wsgi http server
- `djangorestframework-simplejwt` - making auth easier

### Frontend

- `Node 14`
- `react` React
- `react-router-dom` - frontend routing
- `axios` - for making requests
- `Material-UI` - UI libraries

# Development setup

## Without Docker

### Backend

Create a virtual environment from terminal/cmd (or do it in Pycharm manually)

```shell
cd backend

python3 -m venv venv

. venv/Scripts/Activate

python -m pip install --upgrade pip

pip install -r requirements.txt
```

Run django application from terminal/cmd (or add new Django configuration if using Pycharm)

```shell
python manage.py runserver
```

Preparing (if there are any changes to db schema) and running migrations

```
python manage.py makemigrations

python manage.py migrate
```

Create superuser

```shell
python manage.py createsuper user
```

### Frontend

Install node dependencies.

```shell
cd frontend

npm i
```

Run development server in second terminal

```shell
npm start
```

## With Docker

**Make sure Docker Engine is running.**

#### Development configuration

While in **root directory**, build docker images and run them with docker-compose.
This might take up to few minutes.
Rebuilding image is crucial after installing new packages via pip or npm.

```shell
docker-compose up --build
```

Application should be up and running: backend 127.0.0.1:8000, frontend 127.0.0.1:3000, and
nginx 127.0.0.1:8080
If images had been installed and **no changes have been made**, just run to start containers:

```shell script
docker-compose up
```

Bringing down containers with **optional** -v flag removes **all** attached volumes and invalidates caches.

```shell script
docker-compose down
```

To run commands in active container:

```shell script
docker exec -it <CONTAINER_ID/CONTAINER_NAME> <command>
```

e.g

```shell script
docker exec -it backend python manage.py createsuperuser
docker exec -it backend coverage run manage.py test
docker exec -it frontend /bin/sh
```

## CI

This repository uses Github Actions to run test pipeline.  
`pipeline.yml` - runs backend and frontend tests separately

If you want to enable Automatic Deploys, use Heroku dashboard and enable waiting
for CI there.

# Production Deployment

1.  [Create Heroku Account](https://signup.heroku.com/dc)
2.  [Download/Install/Setup Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

    - After install, log into Heroku CLI: `heroku login`

3.  Run: `heroku create <your app name>` to create the Heroku application
4.  Set your environment variables for your production environment by running:

    ```
    heroku config:set PRODUCTION_HOST=<your app name>.herokuapp.com SECRET_KEY=<your secret key>
    ```

5.  Run: `heroku stack:set container` so Heroku knows this is a containerized application
6.  Run: `heroku addons:create heroku-postgresql:hobby-dev` which creates the postgres add-on for Heroku
7.  Deploy your app by running: `git push heroku master`,  
    _or_ by pushing to your github repository,  
    _or_ manually in Heroku dashboard
8.  Go to `<your app name>.herokuapp.com` to see the published website.
