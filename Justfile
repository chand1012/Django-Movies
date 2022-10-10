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

createsuperuser:
    docker compose exec web python manage.py createsuperuser

migrate:
    docker compose exec web python manage.py migrate

logs:
    docker compose logs -f