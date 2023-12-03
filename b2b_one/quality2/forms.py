from django import forms
from .models import QualityTemplateItems

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from django.contrib import messages
from django.utils.safestring import mark_safe

from django.contrib import messages

from django.shortcuts import get_object_or_404

from django.forms import formset_factory

from django.forms.models import inlineformset_factory

from .models import QualityTemplate, QualityTemplateItems, RFIQualitySchedules

from rfi.models import VendorSamplesResponse

class QualityTemplateForm(forms.ModelForm):
    class Meta:
        model = QualityTemplate
        fields = '__all__'

class QualityTemplateItemsForm(forms.ModelForm):
    class Meta:
        model = QualityTemplateItems
        fields = '__all__'

QualityTemplate_Item_FormSet = inlineformset_factory(
    QualityTemplate, QualityTemplateItems, form=QualityTemplateItemsForm,
    extra=0, can_delete=True, can_delete_extra=True
)

class RFIQualitySchedulesForm(forms.ModelForm):
    class Meta:
        model = RFIQualitySchedules
        fields = '__all__'

# Define the formset using formset_factory
RFIQualitySchedulesFormSet = formset_factory(RFIQualitySchedulesForm, extra=0)