# Generated by Django 3.2.16 on 2023-12-01 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfi', '0007_auto_20231201_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfisamples',
            name='sample_status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=100, null=True),
        ),
    ]
