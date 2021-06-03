#!/bin/bash
git checkout dev
git pull
git checkout production
git merge dev
git push
docker-compose down
docker-compose build
docker-compose up -g

