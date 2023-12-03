# Generated by Django 3.2.16 on 2023-12-01 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0001_initial'),
        ('rfi', '0006_rfisamples_sample_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfisamples',
            name='rfi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rfi.rfi'),
        ),
        migrations.AlterField(
            model_name='rfisamples',
            name='sample',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping_list.sl_samples'),
        ),
    ]
