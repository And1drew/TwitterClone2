# Generated by Django 3.1 on 2020-09-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='displayname',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='email',
            field=models.CharField(max_length=120),
        ),
    ]
