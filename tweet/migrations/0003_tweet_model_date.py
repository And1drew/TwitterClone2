# Generated by Django 3.1 on 2020-09-02 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_auto_20200901_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet_model',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
