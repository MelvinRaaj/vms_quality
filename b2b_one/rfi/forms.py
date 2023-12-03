from django import forms
from django.forms import inlineformset_factory

from .models import (
    RFI,VendorsRFI,RFIItem, VendorResponseRFI, VendorSamplesResponse, RFISamples
)

from shopping_list.models import ShoppingList, ShoppingListItem

class RFIForm(forms.ModelForm):
    class Meta:
        model = RFI
        fields = '__all__'  # Include all fields from the RFI model

    # def save(self, commit=True):
    #     rfi_instance = super().save(commit)

    #     # Your logic to populate RFIItem instances
    #     shopping_list_items = ShoppingListItem.objects.filter(shopping_list=rfi_instance.shopping_list)
    #     for shopping_list_item in shopping_list_items:
    #         RFIItem.objects.create(rfi=rfi_instance, rfi_item=shopping_list_item)

    #     return rfi_instance

class RFIItemForm(forms.ModelForm):
    class Meta:
        model = RFIItem
        fields = '__all__'

class RFIVendorResponse_Form(forms.ModelForm):
    class Meta:
        model = VendorsRFI
        fields = '__all__'

class VendorResponseRFI_Form(forms.ModelForm):
    class Meta:
        model = VendorResponseRFI
        fields = '__all__'

class VendorSamplesRFI_Form(forms.ModelForm):
    class Meta:
        model = RFISamples
        fields = '__all__'

class VendorSamplesResponse_Form(forms.ModelForm):
    class Meta:
        model = VendorSamplesResponse
        fields = '__all__'


RFI_Item_FormSet = inlineformset_factory(
    RFI, RFIItem, form=RFIItemForm,
    extra=0, can_delete=True, can_delete_extra=True
)

RFI_Vendor_FormSet = inlineformset_factory(
    RFI, VendorsRFI, form=RFIVendorResponse_Form,
    extra=0, can_delete=True, can_delete_extra=True
)

RFI_Samples_FormSet = inlineformset_factory(
    RFI, RFISamples, form=VendorSamplesRFI_Form,
    extra=0, can_delete=True, can_delete_extra=True
)

VendorResponseRFI_FormSet = inlineformset_factory(
    RFI, VendorResponseRFI, form=VendorResponseRFI_Form,
    extra=0, can_delete=True, can_delete_extra=True
)

VendorSamplesRFI_FormSet = inlineformset_factory(
    RFI, VendorSamplesResponse, form=VendorSamplesResponse_Form,
    extra=0, can_delete=True, can_delete_extra=True
)

