# Generated by Django 2.1.2 on 2019-04-11 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20190405_0213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='iframe',
        ),
    ]
