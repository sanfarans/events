# Generated by Django 3.1.6 on 2021-02-27 14:43

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20210227_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationcode',
            name='code',
            field=models.CharField(default=events.models.random_string, max_length=15),
        ),
    ]
