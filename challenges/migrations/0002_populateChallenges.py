# Generated by Django 3.2.3 on 2021-05-20 18:42

from django.db import migrations


def populate_db(apps, schema_editor):
    Challenge = apps.get_model('challenges', 'Challenge')
    Hint = apps.get_model('challenges', 'Hint')


    challenge_0 = Challenge(flag="JFKDLS$#(*JFAN#R)", title="Level 0", order=0,  hidden=False, description="This level is what we call beginner's luck. You either have it... or ya don't!")
    challenge_0.save()


    hint_0_0 = Hint(challenge=challenge_0, hint="Requires Knowledge of HTML, Browser Developer Tools")
    hint_0_0.save()


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_db)
            ]
