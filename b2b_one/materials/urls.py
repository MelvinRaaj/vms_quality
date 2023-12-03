from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import Fqr
from .views import MaterialsView, MaterialCreateView, MaterialUpdateView, MaterialDeleteView

app_name= "materials"

urlpatterns = [

    path('', MaterialsView.as_view(), name='list_products'),
    path('create/', MaterialCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', MaterialUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', MaterialDeleteView.as_view(), name='delete_product'),

]
