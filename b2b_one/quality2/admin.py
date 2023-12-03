from django.contrib import admin

from .models import (
    QualityTemplateItems, RFIQualitySchedules,QualityTemplate
)

# Register your models here.
admin.site.register(QualityTemplate)
admin.site.register(QualityTemplateItems)
admin.site.register(RFIQualitySchedules)