default:
    just --list

run-fg:
    docker compose up

build:
    docker compose build

rebuild:
    docker compose build --no-cache

run:
    docker compose up -d

stop:
    docker compose down

rm:
    docker compose rm

# If you need to execute commands in the container, use the following first.
console container:
    docker compose exec {{container}} bash

createsuperuser:
    docker compose exec web python manage.py createsuperuser

migrate:
    docker compose exec web python manage.py migrate

makemigrations app:
    docker compose exec web python manage.py makemigrations {{app}}

manage *command:
    docker compose exec web python manage.py {{command}}

logs:
    docker compose logs -f
