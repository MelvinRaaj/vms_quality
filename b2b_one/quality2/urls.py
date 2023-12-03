from django.urls import path
from .views import (QualityTemplateView, QualityTemplateCreate, QualityTemplateUpdate, delete_variant,RFIScheduleUpdate,RFIScheduleUpdate1)

app_name= "quality2"

urlpatterns = [
    # Add your URL patterns here
    path('', QualityTemplateView.as_view(), name='list_products'),
    path('create/', QualityTemplateCreate.as_view(), name='create_product'),
    path('update/<int:pk>/', QualityTemplateUpdate.as_view(), name='update_product'),
    path('delete-variant/<int:pk>/', delete_variant, name='delete_variant'),
    path('update-rfi-schedule', RFIScheduleUpdate, name='update_rfi_schedule'),
    path('update-schedules/<int:pk>/', RFIScheduleUpdate1, name='update_rfi_schedule1'),
    # path('/get_product_names', get_product_names.as_view(), name='get_product_names'),

]
