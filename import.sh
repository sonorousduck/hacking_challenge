#!/bin/bash
rm -i db.sqlite
python3 manage.py migrate
python3 manage.py loaddata db.json
