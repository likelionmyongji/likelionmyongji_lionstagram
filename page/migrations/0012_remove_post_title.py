# Generated by Django 2.1.7 on 2019-04-08 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0011_auto_20190407_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
