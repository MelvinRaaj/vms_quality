from django import forms
from .models import Department

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from django.contrib import messages
from django.utils.safestring import mark_safe

from django.contrib import messages

from django.shortcuts import get_object_or_404


from django.forms import formset_factory

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

    # this function will be used for the validation
    def clean(self):
 
        # data from the form is fetched using super function
        super(DepartmentForm, self).clean()
         
        # extract the username and text field from the data
        department_name = self.cleaned_data.get('department_name')

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department_name'].label = "Department Name"
        self.helper = FormHelper()
        self.helper.form_method = 'post'

# Define the formset using formset_factory
DepartmentFormSet = formset_factory(DepartmentForm, extra=0)
    