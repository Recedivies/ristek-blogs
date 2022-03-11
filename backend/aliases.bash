alias venv=". venv/bin/activate"

alias pmr="python3 manage.py runserver"
alias pmsh="python3 manage.py shell"
alias pmm="python3 manage.py migrate"
alias pmmg="python3 manage.py makemigrations"
alias pmc="python3 manage.py createsuperuser"

alias fresh="rm db.sqlite3 && pmmg && pmm"

alias erd="python manage.py graph_models -a > erd.dot && python manage.py graph_models -a -g -o erd.png"