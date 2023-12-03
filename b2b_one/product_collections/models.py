from django.db import models
from design_spec.models import Designs, Colors


# Create your models here.

class ProductCollection(models.Model):
    ProductCollection_Name = models.CharField(max_length=100, unique=True)
    ProductCollection_Description = models.CharField(max_length=100, unique=False)
    ProductCollection_Image = models.ImageField(upload_to='images/', null=True, blank=True)
    CreateDate = models.DateField(null=True, blank=True)
    LaunchDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.ProductCollection_Name

class Products(models.Model):
    ProductCollection_Name = models.ForeignKey(ProductCollection, on_delete=models.CASCADE)
    Product_Name = models.CharField(max_length=100)
    Product_Description = models.CharField(max_length=100, unique=False)
    Product_Image = models.ImageField(upload_to='images/', null=True, blank=True)
    Product_CreateDate = models.DateField(null=True, blank=True)
    Product_LaunchDate = models.DateField(null=True, blank=True)
    SKU = models.CharField(max_length=100,null=True, blank=True)
    item_code = models.CharField(max_length=100 )
    cbm_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    weight_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Design_Name = models.ForeignKey(Designs, on_delete=models.CASCADE, null=True, blank=True)
    Color_Name = models.ForeignKey(Colors, on_delete=models.CASCADE, null=True, blank=True)

    UOM_CHOICES = (
        ('Meter', 'M'),
        ('Set', 'Set'),
        ('Pcs', 'Pcs'),
        ('KG', 'KG'),
        ('Pack', 'Pack'),
    )
    
    UOM = models.CharField(max_length=100, choices=UOM_CHOICES,null=True, blank=True)
    UOM1 = models.CharField(max_length=100, choices=UOM_CHOICES,null=True, blank=True)
    barcode = models.CharField(max_length=100, null=True, blank=True)

    PRODUCT_STATUS = (
        ('Active', 'Active'),
        ('New', 'New'),
        ('List In', 'List In'),
        ('Discontinued', 'Discontinued'),
    )

    Product_Status = models.CharField(max_length=100, choices=PRODUCT_STATUS)
    status_date = models.DateField(null=True, blank=True)

    sku_material = models.CharField(max_length=100, null=True, blank=True)


    # unique together
    class Meta:
        unique_together = ('ProductCollection_Name', 'Product_Name', 'SKU', 'Design_Name', 'Color_Name')

    def __str__(self):
        return f'{self.ProductCollection_Name} - {self.Product_Name} - {self.SKU} - {self.Design_Name} - {self.Color_Name}'