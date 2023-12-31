# Generated by Django 3.2.16 on 2023-12-01 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rfi', '0012_auto_20231201_1515'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quality2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QualityTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('product_category', models.CharField(blank=True, choices=[('Bedlinen', 'Bedlinen'), ('Bath', 'Bath'), ('Towels', 'Towels'), ('Curtains', 'Curtains'), ('Rugs', 'Rugs'), ('Cushions', 'Cushions'), ('RawMat', 'RawMat'), ('H&L', 'H&L')], max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='qualitytemplateitems',
            name='Result',
        ),
        migrations.CreateModel(
            name='RFIQualitySchedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_date', models.DateField(blank=True, null=True)),
                ('no_of_days', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=100, null=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('quality_template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quality2.qualitytemplateitems')),
                ('samplesresponse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rfi.vendorsamplesresponse')),
            ],
        ),
        migrations.AddField(
            model_name='qualitytemplateitems',
            name='quality_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quality2.qualitytemplate'),
        ),
    ]
