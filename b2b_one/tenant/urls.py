from django.contrib import admin
from django.urls import path

from .views import TenantView

app_name= "tenant"

urlpatterns = [

    path('<str:company>/', TenantView.as_view(), name='tenantview' ),

]
