# Generated by Django 3.2.5 on 2021-07-28 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0023_auto_20210728_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poj',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='poj',
            name='tag_price',
        ),
    ]
