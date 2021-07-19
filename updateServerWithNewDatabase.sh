#!/bin/bash
docker-compose down
git checkout dev
git pull
git checkout production
git merge dev
git push
docker-compose down
python3 manage.py makemigrations
python3 manage.py migrate
docker-compose build
docker-compose up -d

