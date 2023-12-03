from django.urls import path
from .views import (RFIListView, RFI_Create, RFI_Update, delete_variant, delete_vendors,get_product_names,delete_samples)

app_name= "rfi"

urlpatterns = [
    # Add your URL patterns here
    path('', RFIListView.as_view(), name='list_products'),
    path('create/', RFI_Create.as_view(), name='create_product'),
    path('update/<int:pk>/', RFI_Update.as_view(), name='update_product'),
    path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),
    path('delete-samples/<int:pk>/', delete_samples, name='delete_samples'),
    path('delete-vendors/<int:pk>/', delete_variant, name='delete_vendors'),
    path('/get_product_names', get_product_names.as_view(), name='get_product_names'),


]
