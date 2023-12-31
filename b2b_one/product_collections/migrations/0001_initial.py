# Generated by Django 3.2.16 on 2023-11-30 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('design_spec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductCollection_Name', models.CharField(max_length=100, unique=True)),
                ('ProductCollection_Description', models.CharField(max_length=100)),
                ('ProductCollection_Image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('CreateDate', models.DateField(blank=True, null=True)),
                ('LaunchDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=100)),
                ('Product_Description', models.CharField(max_length=100)),
                ('Product_Image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Product_CreateDate', models.DateField(blank=True, null=True)),
                ('Product_LaunchDate', models.DateField(blank=True, null=True)),
                ('SKU', models.CharField(blank=True, max_length=100, null=True)),
                ('item_code', models.CharField(max_length=100)),
                ('cbm_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('weight_unit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('UOM', models.CharField(blank=True, choices=[('Meter', 'M'), ('Set', 'Set'), ('Pcs', 'Pcs'), ('KG', 'KG'), ('Pack', 'Pack')], max_length=100, null=True)),
                ('UOM1', models.CharField(blank=True, choices=[('Meter', 'M'), ('Set', 'Set'), ('Pcs', 'Pcs'), ('KG', 'KG'), ('Pack', 'Pack')], max_length=100, null=True)),
                ('barcode', models.CharField(blank=True, max_length=100, null=True)),
                ('Product_Status', models.CharField(choices=[('Active', 'Active'), ('New', 'New'), ('List In', 'List In'), ('Discontinued', 'Discontinued')], max_length=100)),
                ('status_date', models.DateField(blank=True, null=True)),
                ('sku_material', models.CharField(blank=True, max_length=100, null=True)),
                ('Color_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='design_spec.colors')),
                ('Design_Name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='design_spec.designs')),
                ('ProductCollection_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_collections.productcollection')),
            ],
            options={
                'unique_together': {('ProductCollection_Name', 'Product_Name', 'SKU', 'Design_Name', 'Color_Name')},
            },
        ),
    ]
