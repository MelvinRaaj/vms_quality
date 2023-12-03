from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from shopping_list.models import ShoppingList, ShoppingListItem, SL_Samples

from tenant.models import Tenant

# Create your models here.
class RFI(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    rfi_no = models.CharField(max_length=100, unique=True)
    # Other RFI fields here

    def __str__(self):
        return f'{self.rfi_no} - {self.shopping_list}'

class RFIItem(models.Model):
    rfi = models.ForeignKey(RFI, on_delete=models.CASCADE)
    rfi_item = models.ForeignKey(ShoppingListItem, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.rfi} - {self.rfi_item}'


class RFISamples(models.Model):
    rfi = models.ForeignKey(RFI, on_delete=models.CASCADE,null=True, blank=True)
    sample = models.ForeignKey(SL_Samples, on_delete=models.CASCADE,null=True, blank=True)
    sample_qty = models.IntegerField(default=1)
    # Other RFI sample fields here

    def __str__(self):
        return f'{self.rfi} - {self.sample}'


class VendorsRFI(models.Model):
    rfi = models.ForeignKey(RFI, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Tenant, on_delete=models.CASCADE,null=True, blank=True)
    # Add other fields as needed

    def __str__(self):
        return f'{self.rfi} - {self.vendor}'

@receiver(post_save, sender=VendorsRFI)
def create_vendor_response_rfi(sender, instance, created, **kwargs):
    """
    Signal receiver to create a VendorResponseRFI instance when a VendorsRFI is created.
    """
    if created:
        # If multiple vendors are added at once, 'instance' may be a queryset
        if hasattr(instance, '__iter__'):
            for vendors_rfi in instance:
                # Access RFI items associated with the RFI instance
                rfi_items = RFIItem.objects.filter(rfi=vendors_rfi.rfi)
                
                # Loop through RFI items and create VendorResponseRFI instances for each vendor
                for rfi_item in rfi_items:
                    VendorResponseRFI.objects.create(rfi=vendors_rfi.rfi, rfi_item=rfi_item, vendor=vendors_rfi.vendor)
        else:
            # Access RFI items associated with the single RFI instance
            rfi_items = RFIItem.objects.filter(rfi=instance.rfi)
            
            # Loop through RFI items and create VendorResponseRFI instances for the single vendor
            for rfi_item in rfi_items:
                VendorResponseRFI.objects.create(rfi=instance.rfi, rfi_item=rfi_item, vendor=instance.vendor)

# Connect the signal
post_save.connect(create_vendor_response_rfi, sender=VendorsRFI)


@receiver(post_save, sender=RFISamples)
def create_vendor_samples_response_rfi(sender, instance, created, **kwargs):
    """
    Signal receiver to create a VendorSamplesResponse instance when an RFISamples is created.
    """
    if created:
        # Access vendors associated with the RFISamples instance
        vendors = VendorsRFI.objects.filter(rfi=instance.rfi)
                
        # Loop through vendors and create VendorSamplesResponse instances for each vendor
        for vendor in vendors:
            VendorSamplesResponse.objects.create(
                rfi=instance.rfi,
                vendor=vendor.vendor,
                sample=instance.sample,
                # Add other fields as needed
            )


# Connect the signal
post_save.connect(create_vendor_samples_response_rfi, sender=RFISamples)


# create a model for all responses from each vendor for each item in the RFI
class VendorResponseRFI(models.Model):
    rfi = models.ForeignKey(RFI, on_delete=models.CASCADE)
    rfi_item = models.ForeignKey(RFIItem, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    moq = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    lead_time = models.IntegerField(default=0)
    ETA = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.rfi} - {self.rfi_item} - {self.vendor}'

class VendorSamplesResponse(models.Model):
    rfi = models.ForeignKey(RFI, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    sample = models.ForeignKey(SL_Samples, on_delete=models.CASCADE)
    sample_cost = models.IntegerField(default=0)
    sample_ready_date = models.DateField(null=True, blank=True)
    sample_send_date = models.DateField(null=True, blank=True)
    courier_name = models.CharField(max_length=100,null=True, blank=True)
    courier_tracking_no = models.CharField(max_length=100, null=True, blank=True)
    sample_status_options = (
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('In Transit', 'In Transit'),
        ('PASS', 'PASS'),
        ('FAIL', 'FAIL'),
        ('REDO', 'REDO'),
        ('MRB', 'MRB'),
    )
    sample_status = models.CharField(max_length=100, choices=sample_status_options,null=True, blank=True, default='In Transit')
    
    def __str__(self):
        return f'{self.rfi} - {self.vendor} - {self.sample}'
