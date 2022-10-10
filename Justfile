default:
    just --list

run:
    docker compose up

build:
    docker compose build

rebuild:
    docker compose build --no-cache

run-bg:
    docker compose up -d

stop:
    docker compose down

rm:
    docker compose rm

createsuperuser:
    docker compose exec web python manage.py createsuperuser

migrate:
    docker compose exec web python manage.py migrate