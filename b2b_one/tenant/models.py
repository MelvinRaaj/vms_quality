from django.db import models


tenant_types = (
        ('Main', 'Main'),
        ('Group', 'Group'),
        ('Vendor', 'Vendor'),
        ('Customer', 'Customer'),
    )

class Tenant(models.Model):
    company = models.CharField(max_length=100)
    company_code = models.CharField(max_length=100)
    type = models.CharField(max_length=100,choices=tenant_types, null=True, blank=True, default='Main')
    subdomain_prefix = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.company

class TenantAwareModel(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True


class Tenant_Address(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    Country = models.CharField(max_length=100, null=True, blank=True)
    City = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Postcode = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return f'{self.tenant} - {self.Country} - {self.City} - {self.Address} - {self.Postcode}'
    
class Tenant_Locations(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    location_type_options = (
        ('Factory', 'Factory'),
        ('Warehouse', 'Warehouse'),
        ('Office', 'Office'),
    )

    location_type = models.CharField(max_length=100, choices=location_type_options,null=True, blank=True)
    Country = models.CharField(max_length=100,null=True, blank=True)
    City = models.CharField(max_length=100,null=True, blank=True)
    Address = models.CharField(max_length=100,null=True, blank=True)
    Postcode = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return f'{self.tenant} - {self.location}'