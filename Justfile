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
    docker compose rm --force

clean: rm

# If you need to execute commands in the container, use the following first.
console container="web":
    docker compose exec {{container}} bash

createsuperuser:
    docker compose exec web python manage.py createsuperuser

migrate:
    docker compose exec web python manage.py migrate

makemigrations app *options="":
    docker compose exec web python manage.py makemigrations {{app}} {{options}}

manage *command:
    docker compose exec web python manage.py {{command}}

logs:
    docker compose logs -f

start: run

init: run migrate createsuperuser

get-data:
    wget https://cdn.discordapp.com/attachments/1017871632301309973/1042969879491391578/new_actors.tsv.gz -O actors.tsv.gz
    wget https://cdn.discordapp.com/attachments/1017871632301309973/1042969513114751107/new_movies.tsv.gz -O movies.tsv.gz
    gunzip actors.tsv.gz
    gunzip movies.tsv.gz

clear-data:
    rm actors.tsv
    rm movies.tsv
