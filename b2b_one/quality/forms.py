from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.forms import formset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from .models import QualityTemplateItems, QualityTemplates,QualitySchedules

class QualityTemplateForm(forms.ModelForm):
    class Meta:
        model = QualityTemplates
        fields = '__all__'

    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(QualityTemplateForm, self).clean()
        return self.cleaned_data

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['QualityTemplate_Name'].label = "QualityTemplate Name"

        # Add data widget for Create Date and Launch Date
        self.fields['CreateDate'].widget.attrs['class'] = 'datepicker'

        # Create a helper for crispy forms
        self.helper = FormHelper()
        self.helper.form_method = 'post'

class QualityTemplateItemForm(forms.ModelForm):
    class Meta:
        model = QualityTemplateItems
        fields = '__all__'

    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(QualityTemplateItemForm, self).clean()
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['QualityTemplateItemForm'].label = "QualityTemplateItemForm"

        # Create a helper for crispy forms
        self.helper = FormHelper()
        self.helper.form_method = 'post'

QualityTemplateItemsFormSet = inlineformset_factory(QualityTemplates, QualityTemplateItems, form=QualityTemplateItemForm, extra=1)

# add form for QualitySchedules
class QualityScheduleForm(forms.ModelForm):
    class Meta:
        model = QualitySchedules
        fields = '__all__'

    # this function will be used for the validation
    def clean(self):
        # data from the form is fetched using super function
        super(QualityScheduleForm, self).clean()
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['QualityScheduleForm'].label = "QualityScheduleForm"

        # Create a helper for crispy forms
        self.helper = FormHelper()
        self.helper.form_method = 'post'

