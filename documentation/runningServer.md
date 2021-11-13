# Running the Server

## Wiping the Database
    - Wipe it as we learned for Django. rm db.sqlite3
    - python manage.py migrate

## Run the Server
    - The server is now being ran with uwsgi.
    - To run the server, start a tmux process by typing tmux into the shell
    - Run the ./startServer.sh
    - Press Ctrl + b and then d to leave the session. You can safely close the ssh now
    - To Get back to your server process, run tmux attach

