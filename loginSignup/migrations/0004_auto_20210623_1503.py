# Generated by Django 3.1.4 on 2021-06-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginSignup', '0003_auto_20210604_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='incorrectPerChallenge',
            field=models.JSONField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='numTotalIncorrectGuesses',
            field=models.IntegerField(default=0),
        ),
    ]
