# Generated by Django 3.1.6 on 2021-02-15 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20210215_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
