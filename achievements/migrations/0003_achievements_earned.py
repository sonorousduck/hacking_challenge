# Generated by Django 3.1.4 on 2021-08-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0002_populate'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievements',
            name='earned',
            field=models.BooleanField(default=False),
        ),
    ]
