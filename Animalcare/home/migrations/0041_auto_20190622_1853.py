# Generated by Django 2.1.2 on 2019-06-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0040_auto_20190620_1338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='pages',
        ),
        migrations.AlterField(
            model_name='report',
            name='amount',
            field=models.CharField(max_length=19),
        ),
    ]
