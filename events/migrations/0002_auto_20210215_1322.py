# Generated by Django 3.1.6 on 2021-02-15 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(upload_to=''),
        ),
    ]
