# Creating a Digital Ocean SSH Account

1. Log into the server as root
    a. Log into server, type root
2. Use command: adduser accountname
    a. Note: account must have all lowercase letters
    b. It will prompt for a password. If setting up for someone else, they will be able to change it after account creation.
    c. Prompts also for Full Name, Room Number, Work Phone, Home Phone, and Other. Pressing Enter gives default avalues
3. You can then log onto the server using that new account name. ssh accountname@206.189.210.78
4. Change your password by typing passwd, then the current password, followed by the new password. 
5. Next, in order to access the hacking challenge server, they must be added to the sudo group.
    a. usermod -aG sudo accountname
    b. You can verify this works by trying sudo -i to take you to the root



