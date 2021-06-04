#!/bin/bash
rm -i db.sqlite
python manage.py migrate
python manage.py loaddata db.json

