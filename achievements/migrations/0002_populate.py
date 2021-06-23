# Generated by Django 3.1.4 on 2021-06-23 20:52

from django.db import migrations

# TODO: Add achievementIcon to each of the achievements. That will require me to design a small one for each one. That shouldn't be hard.


def populate_db(apps, schema_editor):
    Achievement = apps.get_model('achievements', 'Achievements')

    achievement_0 = Achievement(title="Flawless", description="You completed these without a single incorrect answer. That is amazing.")
    achievement_0.save()

    achievement_1 = Achievement(title="Completion", description="You finished! Congratulations!")
    achievement_1.save()

    achievement_2 = Achievement(title="Early Bird", description="Complete the hacking challenge within 1.5 weeks of the due date.")
    achievement_2.save()

    achievement_3 = Achievement(title="Class First", description="Complete the assignment first in class")
    achievement_3.save()


    achievement_4 = Achievement(title="Class Second", description="Complete the assignment second in class")
    achievement_4.save()

    achievement_5 = Achievement(title="Class Third", description="Complete the assignment third in class")
    achievement_5.save()


    achievement_6 = Achievement(title="Playing With Fire", description="Complete the assignment within 3 hours of the due date")
    achievement_6.save()


    achievement_7 = Achievement(title="2 down", description="Complete 2 in a row without mistake")
    achievement_7.save()

    achievement_8 = Achievement(title="3 down", description="Complete 3 in a row without mistake")
    achievement_8.save()

    achievement_9 = Achievement(title="Breathtaking", description="Complete 4 in a row without mistake")
    achievement_9.save()

    achievement_10 = Achievement(title="Phenomenal", description="Complete 5 in a row without mistake")
    achievement_10.save()

    achievement_11 = Achievement(title="Unstoppable", description="Complete 6 in a row without mistake")
    achievement_11.save()

    achievement_12 = Achievement(title="Unforgettable", description="Complete 7 in a row without mistake")
    achievement_12.save()

    achievement_13 = Achievement(title="Ascended", description="Complete 8 in a row without mistake")
    achievement_13.save()

    achievement_14 = Achievement(title="Robin Hood", description="Complete the assignment with under 10 incorrect guesses")
    achievement_14.save()

    achievement_15 = Achievement(title="Dead Eye", description="Complete the assignment with under 20 incorrect guesses")
    achievement_15.save()

    achievement_16 = Achievement(title="Sharpshooter", description="Complete the assignment with under 50 incorrect guesses")
    achievement_16.save()

    achievement_17 = Achievement(title="Baby Archer", description="Complete the assignment with under 100 incorrect guesses")
    achievement_17.save()

    achievement_18 = Achievement(title="Committed", description="Complete the assignment with over 200 incorrect guesses")
    achievement_18.save()

    achievement_19 = Achievement(title="Tenacious", description="Complete the assignment with over 300 incorrect guesses")
    achievement_19.save()

    achievement_20 = Achievement(title="Bot Status", description="Complete the assignment with over 750 incorrect guesses")
    achievement_20.save()











class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]
