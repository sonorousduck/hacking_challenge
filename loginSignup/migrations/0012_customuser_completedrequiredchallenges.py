# Generated by Django 3.1.4 on 2021-07-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginSignup', '0011_customuser_percentcomplete'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='completedRequiredChallenges',
            field=models.IntegerField(default=0),
        ),
    ]
