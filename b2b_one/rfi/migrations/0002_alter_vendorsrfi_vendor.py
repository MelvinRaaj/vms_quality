# Generated by Django 3.2.16 on 2023-11-30 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant', '0001_initial'),
        ('rfi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorsrfi',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenant.tenant'),
        ),
    ]
