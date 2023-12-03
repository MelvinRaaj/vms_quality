from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UsernameField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from allauth.account.forms import SignupForm

from django.contrib import messages
from django.utils.safestring import mark_safe

from django.contrib import messages

from django.shortcuts import get_object_or_404

from tenant.models import Tenant
from .models import CustomUser, UserProfile

from phonenumber_field.formfields import PhoneNumberField




class CustomUserCreationForm_Phone(SignupForm):

    phonenumber = forms.CharField()
    company_name = forms.CharField()

    class Meta:
        model = CustomUser
        exclude =('company')
        # fields = ()
        # widgets = {
        #     'phonenumber': forms.TextInput(
        #         attrs={}
        #         )
        # }

    # this function will be used for the validation
    def clean(self):
 
        # data from the form is fetched using super function
        super(CustomUserCreationForm_Phone, self).clean()
         
        # extract the username and text field from the data
        company_name = self.cleaned_data.get('company_name')
        phone = self.cleaned_data.get('phonenumber')



        # emails = self.cleaned_data.get('email')

        try:
            tenant = Tenant.objects.get(company=company_name)  
        except Tenant.DoesNotExist:
            tenant = None

        # conditions to be met for Company (Tenant)
        if tenant:
            self._errors['company_name'] = self.error_class([
                'Company with name {} already is registered with B2B_One!'.format(company_name)])
        else:
            pass

        try:
            phones = CustomUser.objects.get(phone=phone)  
        except CustomUser.DoesNotExist:
            phones = None

        if phones:
            self._errors['phonenumber'] = self.error_class([
                'Phone number {} already with is registered B2B_One!'.format(phone)])
        else:
            pass

        # return any errors if found
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phonenumber'].label = "Your Phone Number"
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # NOt used as "crispy form" in template was replaced with form|cripsy
        # self.helper.add_input(Submit('submit', 'Submit'))


class CustomUserCreationForm_Invite(SignupForm):

    class Meta:
        model = CustomUser
        # fields = ('email','user_role',)
        fields = ('email')
        # widgets = {
        #     'company': forms.TextInput(
        #         attrs={}
        #         )
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['email'].label = "Your Email"
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     # NOt used as "crispy form" in template was replaced with form|cripsy
    #     # self.helper.add_input(Submit('submit', 'Submit'))

    # # this function will be used for the validation
    # def clean(self):
 
    #     # data from the form is fetched using super function
    #     super(CustomUserCreationForm_Invite, self).clean()
         
    #     # extract the username and text field from the data
    #     company_name = self.cleaned_data.get('company_name')

    #     # emails = self.cleaned_data.get('email')

    #     try:
    #         tenant = Tenant.objects.get(company=company_name)  
    #     except Tenant.DoesNotExist:
    #         tenant = None

    #     # conditions to be met for Company (Tenant)
    #     if tenant:
    #         self._errors['company_name'] = self.error_class([
    #             'Company with name {} already exists!'.format(company_name)])
    #     else:
    #         pass

    #     #BLANKED OUT DUE TO ALLAUTH SEND EMAIL REMINDER IF TRYING TO REREGISTER
    #     # try:
    #     #     emails =CustomUser.objects.get(email=emails)  
    #     # except CustomUser.DoesNotExist:
    #     #     emails = None

    #     # if emails:
    #     #     self._errors['email'] = self.error_class([
    #     #         'Email with address {} already exists!'.format(emails)])
    #     # else:
    #     #     pass

    #     # return any errors if found
    #     return self.cleaned_data


class CustomUserCreationForm(SignupForm):

    company_name = forms.CharField()

    class Meta:
        model = CustomUser
        exclude =('company')
        fields = ('email')
        # widgets = {
        #     'company': forms.TextInput(
        #         attrs={}
        #         )
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = "Your Email"
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # NOt used as "crispy form" in template was replaced with form|cripsy
        # self.helper.add_input(Submit('submit', 'Submit'))

    # this function will be used for the validation
    def clean(self):
 
        # data from the form is fetched using super function
        super(CustomUserCreationForm, self).clean()
         
        # extract the username and text field from the data
        company_name = self.cleaned_data.get('company_name')

        # emails = self.cleaned_data.get('email')

        try:
            tenant = Tenant.objects.get(company=company_name)  
        except Tenant.DoesNotExist:
            tenant = None

        # conditions to be met for Company (Tenant)
        if tenant:
            self._errors['company_name'] = self.error_class([
                'Company with name {} already exists!'.format(company_name)])
        else:
            pass

        #BLANKED OUT DUE TO ALLAUTH SEND EMAIL REMINDER IF TRYING TO REREGISTER
        # try:
        #     emails =CustomUser.objects.get(email=emails)  
        # except CustomUser.DoesNotExist:
        #     emails = None

        # if emails:
        #     self._errors['email'] = self.error_class([
        #         'Email with address {} already exists!'.format(emails)])
        # else:
        #     pass

        # return any errors if found
        return self.cleaned_data



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email','user_role',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (

            'user_first_name',
            'user_last_name',
            'user_position',
            'user_birthdate',
            'user_id',
            'user_facebook',
            'user_linkedin',
            'user_phone',
            'user_status',
            
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-UserProfileForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_class = 'blueForms'
        self.helper.layout = Layout(
            'user_first_name',
            'user_last_name',
            'user_position',
            'user_birthdate',
            'user_id',
            'user_facebook',
            'user_linkedin',
            'user_phone',
            'user_status',
        )
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
