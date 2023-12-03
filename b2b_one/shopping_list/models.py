from django.db import models
from products.models import Product_Collection, Product_SKU

from tenant.models import Tenant


# Create your models here.
class ShoppingList(models.Model):
    shopping_list = models.CharField(max_length=100)
    collection = models.ForeignKey(Product_Collection, on_delete=models.CASCADE,null=True, blank=True)
    description = models.CharField(max_length=100, unique=False)

    main_pr_type = (
        ('Trade', 'Trade'),
        ('Non Trade', 'Non Trade'),
    )

    main_pr_type = models.CharField(max_length=100, choices=main_pr_type,null=True, blank=True, default='Trade')

    pr_category = (
        ('Import', 'Import'),
        ('Local', 'Local'),
    )

    pr_category = models.CharField(max_length=100, choices=pr_category,null=True, blank=True, default='Import')

    pr_product = (
        ('FG', 'FG'),
        ('RAWMAT', 'RAWMAT'),
        ('S-FG', 'S-FG'),
    )

    pr_product = models.CharField(max_length=100, choices=pr_product,null=True, blank=True)

    plan_otf = models.DateField(null=True, blank=True)
    created = models.DateField(null=True, blank=True)
    updated = models.DateField(null=True, blank=True)

    sl_status = (
        ('Draft', 'Draft'),
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Closed', 'Closed'),
    )

    sl_status = models.CharField(max_length=100, choices=sl_status,null=True, blank=True)
    status_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.shopping_list} - {self.collection} - {self.plan_otf}'

        
class ShoppingListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE, null=True, blank=True)
    product_sku = models.ForeignKey(Product_SKU, on_delete=models.CASCADE, null=True, blank=True)
    expected_receive_date = models.DateField(null=True, blank=True)
    launch_date = models.DateField(null=True, blank=True)
    delivery_location = models.CharField(max_length=100, unique=False)
    qty = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.shopping_list} - {self.product_sku} - {self.qty}'

class bedlinen_fabrics(models.Model):

    name_options = (
        ('TENCEL LYOCELL', 'TENCEL LYOCELL'),
        ('TENCEL MODAL', 'TENCEL MODAL'),
        ('BAMBOO', 'BAMBOO'),
        ('LONG STAPLE COTTON', 'LONG STAPLE COTTON'),
        ('COTTON', 'COTTON'),
        ('POLY TENCEL', 'POLY TENCEL'),
        ('SAME AS SKU', 'SAME AS SKU'),
    )

    line_options = (
        ('ROTARY REACTIVE PRINT', 'ROTARY REACTIVE PRINT'),
        ('ROTARY DISPERSE PRINT 圆网分散印花', 'ROTARY DISPERSE PRINT 圆网分散印花'),
        ('SAME AS SKU', 'SAME AS SKU'),
    )

    bedlinen_name = models.CharField(max_length=100, choices=name_options,null=True, blank=True)
    line = models.CharField(max_length=100, choices=line_options,null=True, blank=True)
    composition = models.CharField(max_length=100, unique=False)
    country = models.CharField(max_length=100, unique=False)

    # need to link this to the surcharge models

    def __str__(self):
        return self.bedlinen_name + ' - ' + self.line + ' - ' + self.country


class SL_Samples(models.Model):

    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE,null=True, blank=True)
    product_sku = models.ForeignKey(Product_SKU, on_delete=models.CASCADE,null=True, blank=True)
    sample_send_date = models.DateField(null=True, blank=True)

    sample_type = (
        ('NPI', 'NPI'),
        ('PP', 'PP'),
        ('SS', 'SS'),
        ('Lab Dip', 'Lab Dip'),
    )

    sample_type = models.CharField(max_length=100, choices=sample_type,null=True, blank=True)

    bedlinen_name = models.ForeignKey(bedlinen_fabrics, on_delete=models.CASCADE,null=True, blank=True)
    sample_qty = models.IntegerField(null=True, blank=True)
    status_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.shopping_list} - {self.product_sku} - {self.sample_qty}'


