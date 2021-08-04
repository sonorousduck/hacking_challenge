# Scores

## Determining Due Date
    - On the custom admin page, due dates and opening dates for the assignment can be determined.
    - This will stop progress of required challenges, but will allow the student to continue through the assignment

## Setting up the automatic email system
    - Access the automatic system by using crontab -e.
    - Here you can configure the automatic database backup system, along with creating the scores.csv file, and emailing it. Change the gmail address to whatever address is desired for the person grading the assignment.
    - Look up crontab stuff to change anything else, but you then configure the 5 values in front to determine what time to automatically send you the email. Change it to be whatever time and date the assignment is due

    i.e 
    0 0 5 12 * To have it automatically email at 0:00 on the 5th of December, on any day of the week (The * determines what specific day of the week, like Monday)


