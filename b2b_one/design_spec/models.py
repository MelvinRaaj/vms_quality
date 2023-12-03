from django.db import models

# Create your models here.

class Designs(models.Model):
    Design_Name = models.CharField(max_length=100, unique=True)
    Design_Description = models.CharField(max_length=100, unique=False)
    Design_Image = models.ImageField(upload_to='images/', null=True, blank=True)
    CreateDate = models.DateField(null=True, blank=True)
    LaunchDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.Design_Name
    

class Colors(models.Model):
    Color_Name = models.CharField(max_length=100, unique=True)
    Design_Name = models.ForeignKey(Designs, on_delete=models.CASCADE)
    Color_Description = models.CharField(max_length=100, unique=False)
    Color_Image = models.ImageField(upload_to='images/', null=True, blank=True)
    CreateDate = models.DateField(null=True, blank=True)
    LaunchDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.Design_Name + ' - ' + self.Color_Name
