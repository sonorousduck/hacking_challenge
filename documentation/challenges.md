# Challenges

## Creating New Challenges
    - You can add on to the current version by going to aggiectf.tk/admin and going to challenges and adding one from there. Additionally, add it to the migration script as well.
    - There is a Challenge model and a Hint Model.

### Challenge
    - flag: This is the password
    - title: The title for the Challenge.
    - Description: Description for the challenge, not the hints though
    - Order: Does the order for the challenge to appear in the assignment
    - TemplateValue: This is to tie it to a certain html file that you write for each individual challenge. This allows you to change the order of the challenges without messing up the html file it points to.
    - hidden: Outdated model entry. This probably should be deleted.
    - pointValue: Calculates the value of the challenges
    - optionalChallenge: Indicates the optional challenges. This is used to calculate the percentage of completed items for the percent score the student has completed (Default False)
    - difficultyIndicator: Determines in which section the challenge gets put. Currently there exists "Easy", "Moderate", and "Hard"
    - challengeSeries: Not really used, but could be useful
    - totalIncorrectGuesses: Used to track difficulty of the challenge. High incorrect guesses is more difficult (Most likely)
    - numberOfUsersOnThisChallenge: Want to implement this eventually. Along with tracking the amount of time that is spent on it
 

### Hint
    - challenge: Determines to which challenge the hint is associated with
    - hint: Description of the hint.
