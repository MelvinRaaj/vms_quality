from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import Fqr
from .views import Shopping_List_View

app_name= "shopping_list"

urlpatterns = [

    path('', Shopping_List_View.as_view(), name='list_products'),
    # path('create/', ProductCreate.as_view(), name='create_product'),
    # path('update/<int:pk>/', ProductUpdate.as_view(), name='update_product'),
    # path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),

]
