#!/bin/bash

args=("$@")

command="${args[0]}"

if [ $command = "pmm" ]; then

    python3 manage.py migrate

elif [ $command = "pmr" ]; then

    python3 manage.py runserver

elif [ $command = "pmmg" ]; then

    python3 manage.py makemigrations

elif [ $command = "pmc" ]; then

    python3 manage.py createsuperuser

elif [ $command = "pmsh" ]; then

    python3 manage.py shell

else

    echo "Invalid Command"

fi




