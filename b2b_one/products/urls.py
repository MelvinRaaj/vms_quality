from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import Fqr
from .views import CollectionView, ProductCreate, ProductUpdate, delete_variant, delete_material

app_name= "products"

urlpatterns = [

    path('', CollectionView.as_view(), name='list_products'),
    path('create/', ProductCreate.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update_product'),
    path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),
    path('delete_material/<int:pk>/', delete_material, name='delete_material'),

]
