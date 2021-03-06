# Generated by Django 3.2.5 on 2021-07-31 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0025_remove_poj_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='poj',
            name='currency',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='firstapp.currency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poj',
            name='rate',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poj',
            name='tag_price',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='poj',
            name='center_stone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.centerstone'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='cert',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.certificate'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='color_of_center_stone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.colorofcstone'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='jewellery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.jewell'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.loc'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='metal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.metal1'),
        ),
        migrations.AlterField(
            model_name='poj',
            name='shape',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='firstapp.shape1'),
        ),
    ]
