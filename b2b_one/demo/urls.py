from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import Fqr
from .views import FqrView, QualitySchedule, ProductUpdate, ProductCreate, ProductList, delete_image, delete_variant

app_name= "demo"

urlpatterns = [
    # path('', FqrView, name='FqrView'),
    path('quality_scheduler/', QualitySchedule, name='QualitySchedule'),

    path('', ProductList.as_view(), name='list_products'),
    path('create/', ProductCreate.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='update_product'),
    path('delete-image/<int:pk>/', delete_image, name='delete_image'),
    path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),

]
