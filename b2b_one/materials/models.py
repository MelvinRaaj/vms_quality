from django.db import models

# Create your models here.
class Materials(models.Model):

    material_name = models.CharField(max_length=100, unique=True)
    fabric_type_material = (
        ('TENCEL LYOCELL','TENCEL LYOCELL'),
        ('TENCEL MODAL','TENCEL MODAL'),
        ('BAMBOO','BAMBOO'),
        ('LONG STAPLE COTTON','LONG STAPLE COTTON'),
        ('COTTON','COTTON'),
        ('COTTON with ADM','COTTON with ADM'),
        ('COTTON, POLYCOTTON','COTTON, POLYCOTTON'),
        (' POLYESTER (75gsm - 90gsm)',' POLYESTER (75gsm - 90gsm)'),
        (' POLYESTER (>100gsm)',' POLYESTER (>100gsm)'),
        ('MICRO TENCEL COTTON  ','MICRO TENCEL COTTON  '),
        ('TENCEL BAMBOO CHARCOAL ','TENCEL BAMBOO CHARCOAL '),
        ('SUPIMA COTTON','SUPIMA COTTON'),
        ('POLYESTER (75gsm - 90gsm)','POLYESTER (75gsm - 90gsm)'),
        ('POLYESTER (>100gsm)','POLYESTER (>100gsm)'),
        ('Others','Others'),
    )   
    material_type = models.CharField(max_length=100, unique=False, choices=fabric_type_material)


    def __str__(self):
        return f'{self.material_name} - {self.material_type}'