from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import QualityHome, qualitytemplatelist, qualitytemplatelistcreate, QualitySchedulesView, Samples,QualitySchedules1,InspectionSchedules1,InspectionItemSchedules1,InspectionItemAQL

app_name= "quality"

urlpatterns = [
    path('/', QualityHome.as_view(), name='QualityHome'),
    path('/schedule', QualitySchedulesView, name='QualitySchedules'),
    path('/schedule1', QualitySchedules1.as_view(), name='QualitySchedules1'),
    path('/inspections', InspectionSchedules1.as_view(), name='InspectionSchedules1'),
    path('/inspection_details', InspectionItemSchedules1.as_view(), name='InspectionItemSchedules1'),
    path('/inspection_details/AQL', InspectionItemAQL.as_view(), name='InspectionItemAQL'),
    path('/list', qualitytemplatelist, name='qualitytemplatelist'),
    path('/samples', Samples.as_view(), name='samples'),


    # For creating a new QualityTemplates
    path('create/', qualitytemplatelistcreate.as_view(), name='create_quality'),

    # For updating an existing QualityTemplates
    # path('update/<int:pk>/', QualityTemplatesUpdateView, name='update_quality'),

    # path('update_all/', product_collections_update_all, name='product_collections_update_all'),
    # path('/<int:pk>/update/', product_collections_update, name='product_collections_update'),
    # path('<int:pk>/delete/', product_collections_delete, name='product_collections_delete'),

]
