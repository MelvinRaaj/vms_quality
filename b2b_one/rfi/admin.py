from django.contrib import admin

from .models import RFI, RFIItem, VendorsRFI, VendorResponseRFI, RFISamples, VendorSamplesResponse

# Register your models here.
admin.site.register(RFI)
admin.site.register(RFIItem)
admin.site.register(VendorsRFI)
admin.site.register(VendorResponseRFI)
admin.site.register(RFISamples)
admin.site.register(VendorSamplesResponse)

