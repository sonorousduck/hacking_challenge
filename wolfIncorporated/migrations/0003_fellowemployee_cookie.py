# Generated by Django 3.1.4 on 2021-06-08 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wolfIncorporated', '0002_fellowemployee'),
    ]

    operations = [
        migrations.AddField(
            model_name='fellowemployee',
            name='cookie',
            field=models.CharField(default='A4B00DPG', max_length=20),
            preserve_default=False,
        ),
    ]
