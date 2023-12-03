# Generated by Django 3.2.16 on 2023-12-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality2', '0009_alter_rfiqualityschedules_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfiqualityschedules',
            name='Line_Result_Value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='rfiqualityschedules',
            name='Variance_Percentage',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='rfiqualityschedules',
            name='Variance_Value',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='rfiqualityschedules',
            name='no_of_days',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
