# Generated by Django 2.1.7 on 2019-04-06 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0010_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]