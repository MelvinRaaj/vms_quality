from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import Fqr
from .views import Shopping_List_View, SL_Line_Create, SL_Line_Update, delete_variant, delete_samples, get_product_names

app_name= "shopping_list"

urlpatterns = [

    path('', Shopping_List_View.as_view(), name='list_products'),
    path('create/', SL_Line_Create.as_view(), name='create_product'),
    path('update/<int:pk>/', SL_Line_Update.as_view(), name='update_product'),
    path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),
    path('delete-samples/<int:pk>/', delete_samples, name='delete_samples'),
    path('/get_product_names', get_product_names.as_view(), name='get_product_names'),
    # path('product-sku-autocomplete/', ProductSKUAutocomplete.as_view(), name='product-sku-autocomplete'),

]
