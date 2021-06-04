# Instructions for updating
- Log into CTFD-admin
- Type root to navigate to the root user
- cd into hacking_challenge
- Run updateServer.sh
    - This will take care of all the merging of the production and dev branches and rebuild the server and bring the server back up again automatically.


# Instructions for Server Backups
- Run export.sh, which will automatically create a backup in a file called db.json
- For importing the backup, run import.sh, and that will take care of all the migrations and importing the database


