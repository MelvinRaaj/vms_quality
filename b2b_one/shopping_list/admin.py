from django.contrib import admin
from .models import ShoppingList, ShoppingListItem, SL_Samples, bedlinen_fabrics


# Register your models here.
admin.site.register(ShoppingList)
admin.site.register(ShoppingListItem)
admin.site.register(SL_Samples)
admin.site.register(bedlinen_fabrics)

