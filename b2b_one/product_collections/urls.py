from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductCollectionListView, ProductsInline, ProductUpdate, ProductCreate
app_name= "product_collections"

urlpatterns = [
    path('/', ProductCollectionListView.as_view(), name='product_collections_list'),
    path('create/', ProductCreate.as_view(), name='create_product_collection'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='edit_product_collection'),
    # path('<int:pk>/edit/', ProductCreate.as_view(), name='create_product_collection'),
    # path('<int:pk>/edit/', ProductUpdate.as_view(), name='edit_product_collection'),


]
