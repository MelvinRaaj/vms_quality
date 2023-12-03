# Generated by Django 3.2.16 on 2023-12-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality2', '0008_auto_20231203_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rfiqualityschedules',
            name='Result',
            field=models.CharField(blank=True, choices=[('N/A', 'N/A'), ('Pass', 'Pass'), ('Fail', 'Fail'), ('Redo', 'Redo')], default='N/A', max_length=100, null=True),
        ),
    ]
