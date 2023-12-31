# Generated by Django 3.2.16 on 2023-12-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quality2', '0004_auto_20231201_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualitytemplateitems',
            name='Attachments',
        ),
        migrations.RemoveField(
            model_name='qualitytemplateitems',
            name='Comments',
        ),
        migrations.RemoveField(
            model_name='qualitytemplateitems',
            name='Date_Of_Test',
        ),
        migrations.RemoveField(
            model_name='qualitytemplateitems',
            name='Test_By',
        ),
        migrations.AlterField(
            model_name='qualitytemplateitems',
            name='Test_Property',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='qualitytemplateitems',
            name='Test_Requirement',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='qualitytemplateitems',
            name='Test_Standard',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='qualitytemplateitems',
            name='Testing_Line',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
