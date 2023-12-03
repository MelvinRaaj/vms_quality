from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from .views import DepartmentListView
from .views import department_list, department_edit, department_delete, department_create, department_update_all

app_name= "department"

urlpatterns = [
    path('/', department_list, name='department_list'),
    path('department/create/', department_create, name='department_create'),
    path('department/update_all/', department_update_all, name='department_update_all'),
    path('department/<int:pk>/edit/', department_edit, name='department_edit'),
    path('department/<int:pk>/delete/', department_delete, name='department_delete'),
]
