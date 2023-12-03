from django.contrib import admin
from .models import Product_Collection, Product_SKU, Product_Country


admin.site.register(Product_Collection)
admin.site.register(Product_SKU)
admin.site.register(Product_Country)
# Register your models here.
