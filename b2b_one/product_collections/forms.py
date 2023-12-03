from django import forms
from .models import ProductCollection, Products

from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.forms import formset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class ProductCollectionForm(forms.ModelForm):
    class Meta:
        model = ProductCollection
        fields = '__all__'

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        exclude = ['ProductCollection_Name']  # Exclude the foreign key as it will be handled in the view



ProductCollectionsFormSet = inlineformset_factory(
    ProductCollection, Products, form=ProductsForm,
    extra=1, can_delete=True, can_delete_extra=True
)

