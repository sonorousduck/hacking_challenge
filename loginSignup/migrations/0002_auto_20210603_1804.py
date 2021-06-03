# Generated by Django 3.1.4 on 2021-06-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginSignup', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-completedChallenges']},
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='numChallenges',
            field=models.IntegerField(default=0),
        ),
    ]
