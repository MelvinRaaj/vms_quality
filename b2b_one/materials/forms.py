from django import forms
from django.forms import inlineformset_factory

from .models import (
    Materials
)

class Material_Form(forms.ModelForm):

    class Meta:
        model = Materials
        fields = '__all__'
