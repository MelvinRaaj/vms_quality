from django.contrib.auth.models import Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from materials.models import Materials

from rfi.models import VendorSamplesResponse

from users.models import CustomUser

# Create your models here.

class QualityTemplate(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
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
    
    product_category = models.CharField(max_length=100, choices=product_category,)
    material = models.ForeignKey(Materials, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name


class QualityTemplateItems(models.Model):
    quality_template = models.ForeignKey(QualityTemplate, on_delete=models.CASCADE,null=True, blank=True)
    Test_Property = models.CharField(max_length=100, null=True, blank=True)
    Test_Standard = models.CharField(max_length=100, null=True, blank=True)
    Standard_Quality_Information = models.CharField(max_length=100, unique=False)
    Test_Requirement = models.CharField(max_length=100, null=True, blank=True)
    Requirement_Lower_Range = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Requirement_Upper_Range = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Testing_Line = models.CharField(max_length=100, null=True, blank=True)
    dim = models.CharField(max_length=100,null=True, blank=True)
    Spec_Value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
       return f'{self.quality_template}'

# create a signal to detect VendorSamplesResponse creation
# create RFIQualitySchedules for each VendorSamplesResponse
# create a signal to detect VendorSamplesResponse update
# update RFIQualitySchedules for each VendorSamplesResponse

@receiver(post_save, sender=VendorSamplesResponse)
def create_rfi_quality_schedules(sender, instance, created, **kwargs):
    """
    Signal receiver to create a RFIQualitySchedules instance when a VendorSamplesResponse is created.
    """
    if created:
        # Get the QualityTemplate associated with the product_sku
        product_category = instance.sample.product_sku.product_category
        print(product_category)
        quality_template = QualityTemplate.objects.get(product_category=product_category)
        print(quality_template)

        # Filter QualityTemplateItems based on the QualityTemplate
        quality_template_items = QualityTemplateItems.objects.filter(
            quality_template=quality_template,
        )

        # Loop through QualityTemplateItems and create RFIQualitySchedules instances for each item
        for quality_template_item in quality_template_items:
            RFIQualitySchedules.objects.create(
                quality_template=quality_template_item,
                samplesresponse=instance,
            )

# Connect the signal
post_save.connect(create_rfi_quality_schedules, sender=VendorSamplesResponse)

class RFIQualitySchedules (models.Model):
    quality_template = models.ForeignKey(QualityTemplateItems, on_delete=models.CASCADE,null=True, blank=True)
    samplesresponse = models.ForeignKey(VendorSamplesResponse, on_delete=models.CASCADE,null=True, blank=True)
    status_option = (
        ('Not Scheduled', 'Not Scheduled'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=100, choices=status_option,null=True, blank=True, default='Not Scheduled')
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True, blank=True)
    assigned_date = models.DateField(null=True, blank=True)
    no_of_days = models.IntegerField(null=True, blank=True,default=0)
    Line_Result_Value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    Variance_Value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,default=0)
    Variance_Percentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,default=0)

    result_options = (
        ('N/A', 'N/A'),
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
        ('Redo', 'Redo'),
    )

    Result = models.CharField(max_length=100, choices=result_options,null=True, blank=True, default='N/A')
    Comments = models.CharField(max_length=100, null=True, blank=True)
    test_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.quality_template} - {self.samplesresponse}'
    

