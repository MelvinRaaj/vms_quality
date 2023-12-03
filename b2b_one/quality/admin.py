from django.contrib import admin
from .models import QualityTemplates, QualityTemplateItems, QualitySchedules,QualitySamples
# Register your models here.
admin.site.register(QualityTemplates)
admin.site.register(QualityTemplateItems)
admin.site.register(QualitySchedules)
admin.site.register(QualitySamples)