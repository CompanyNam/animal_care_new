# Generated by Django 2.1.2 on 2019-03-28 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20190328_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='home',
        ),
    ]