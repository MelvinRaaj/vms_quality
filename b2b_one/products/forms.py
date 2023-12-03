from django import forms
from django.forms import inlineformset_factory

from .models import (
    Product_Collection, Product_SKU, Materials
)


class CollectionForm(forms.ModelForm):

    class Meta:
        model = Product_Collection
        fields = '__all__'


class Product_SKU_Form(forms.ModelForm):

    class Meta:
        model = Product_SKU
        fields = '__all__'

class MaterialsForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = '__all__'

Product_SKU_FormSet = inlineformset_factory(
    Product_Collection, Product_SKU, form=Product_SKU_Form,
    extra=0, can_delete=True, can_delete_extra=True
)

Collection_Material_FormSet = inlineformset_factory(
    Product_Collection, Materials, form=MaterialsForm,
    extra=0, can_delete=True, can_delete_extra=True
)