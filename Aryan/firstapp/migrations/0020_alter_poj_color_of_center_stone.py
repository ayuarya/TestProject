# Generated by Django 3.2.5 on 2021-07-28 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0019_auto_20210728_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poj',
            name='color_of_center_stone',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.PROTECT, to='firstapp.colorofcstone'),
            preserve_default=False,
        ),
    ]
