# Running the Server

## Wiping the Database
    - Wipe it as we learned for Django. rm db.sqlite3
    - python manage.py migrate

## Run the Server
    - Running the server was done with docker
    - There is a script to make sure the server is automatically set up correctly. Run this with ./updateServer.sh
    - Alternatively, make sure the server is taken down with docker-compose down.
    - Then rebuild the server with docker-compose build
    - Then run the server with docker-compose up


    So:
        docker-compose down
        docker-compose build (This should take care of installing any required python files)
        docker-compose up


