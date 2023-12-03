from django.db import models
from design_spec.models import Designs, Colors

from materials.models import Materials

class Product_Collection(models.Model):
    Brand_Name = models.CharField(max_length=100)
    Collection_Name = models.CharField(max_length=100, unique=True)

    collection_product_category = (
            ('Bedlinen', 'Bedlinen'),
            ('Bath', 'Bath'),
            ('Towels', 'Towels'),
            ('Curtains', 'Curtains'),
            ('Rugs', 'Rugs'),
            ('Cushions', 'Cushions'),
            ('RawMat', 'RawMat'),
            ('H&L', 'H&L'),
            ('Mix', 'Mix'),
        )
    
    collection_product_category = models.CharField(max_length=100, choices=collection_product_category,null=True, blank=True)

    Collection_Description = models.CharField(max_length=100, unique=False)
    CreateDate = models.DateField(null=True, blank=True)
    LaunchDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.Brand_Name + ' - ' + self.Collection_Name

class Product_Country(models.Model):

    #country options
    country_options = (
        ('MY', 'MY'),
        ('SG', 'SG'),
        ('KN', 'KN'),
        ('PH', 'PH'),
        ('VN', 'VN'),   
    )

    #country options
    company_options = (
        ('Eastern Decorator Sdn Bhd', 'Eastern Decorator Sdn Bhd'),
        ('Eadess SG Pte Ltd', 'Eadess SG Pte Ltd'),
        ('Akemi International (M) Sdn Bhd', 'Akemi International (M) Sdn Bhd'),        
    )

    Product_Country = models.CharField(max_length=100, choices=country_options)
    Company = models.CharField(max_length=100, choices=company_options)

    def __str__(self):
        return self.Product_Country + ' - ' + self.Company

class Product_SKU(models.Model):
    Collection_Name = models.ForeignKey(Product_Collection, on_delete=models.CASCADE)
    Product_Country = models.ForeignKey(Product_Country, on_delete=models.CASCADE, null=True, blank=True)
    Product_Name = models.CharField(max_length=100)

    # We need a main category table here
    product_category = (
            ('Bedlinen', 'Bedlinen'),
            ('Bath', 'Bath'),
            ('Towels', 'Towels'),
            ('Curtains', 'Curtains'),
            ('Rugs', 'Rugs'),
            ('Cushions', 'Cushions'),
            ('RawMat', 'RawMat'),
            ('H&L', 'H&L'),
        )
    
    product_category = models.CharField(max_length=100, choices=product_category,null=True, blank=True)
    pcs_set = models.CharField(max_length=100, null=True, blank=True)
    Product_Description = models.CharField(max_length=100, unique=False)
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
    M1 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    M2 = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    M_Coor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    M_Panel = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.Collection_Name} - {self.Product_Country} - {self.Product_Name} - {self.SKU} - {self.Design_Name} - {self.Color_Name}'

    # unique together
    class Meta:
        unique_together = ('Collection_Name', 'Product_Name', 'SKU', 'Design_Name', 'Color_Name')
    
class Materials(models.Model):

    Product_Collection = models.ForeignKey(Product_Collection, on_delete=models.CASCADE, null=True, blank=True)
    fabric_type_options = (
        ('M1','M1'),
        ('M2','M2'),
        ('M Coor','M Coor'),
        ('M Panel','M Panel'),
        ('Others','Others'),
        ('N/A','N/A'),
    )

    Fabric_Type = models.CharField(max_length=100, unique=False, choices=fabric_type_options)
    material_name = models.ForeignKey(Materials, on_delete=models.CASCADE, null=True, blank=True)    
    Fabric_Composition = models.CharField(max_length=100, unique=False)
    Yarn_Count_Warp = models.CharField(max_length=100, unique=False)
    Yarn_Count_Weft = models.CharField(max_length=100, unique=False)
    Greige_Construction_Warp = models.CharField(max_length=100, unique=False)
    Greige_Construction_Weft = models.CharField(max_length=100, unique=False)
    Finished_Construction_Warp = models.CharField(max_length=100, unique=False)
    Finished_Construction_Weft = models.CharField(max_length=100, unique=False)
    Finished_Width_CM = models.CharField(max_length=100, unique=False)
    Usable_Width_CM = models.CharField(max_length=100, unique=False)
    Fabric_Weight_GSM = models.CharField(max_length=100, unique=False)
    Weaving_Structure = models.CharField(max_length=100, unique=False)

    def __str__(self):
        return f'{self.ProductCollection} - {self.Fabric_Type} - {self.material_name}'

# add signal to create a design and color when a product is created
# from django.db.models.signals import post_save

# def create_design(sender, instance, created, **kwargs):
#     if created:
#         Designs.objects.create(Product_Name=instance)   
#         Colors.objects.create(Product_Name=instance)
