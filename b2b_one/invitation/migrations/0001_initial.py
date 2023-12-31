# Generated by Django 3.2.16 on 2023-11-30 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False, verbose_name='accepted')),
                ('key', models.CharField(max_length=64, unique=True, verbose_name='key')),
                ('sent', models.DateTimeField(null=True, verbose_name='sent')),
                ('phone', models.CharField(blank=True, max_length=300, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='e-mail address')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
