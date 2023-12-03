from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

import json

from django import forms
from django.contrib import messages

from django.shortcuts import get_object_or_404

from tenant.models import Tenant

from phonenumber_field.formfields import PhoneNumberField

from invitations.forms import InviteForm
from .models import CustomInvitation

from django.forms import formset_factory

from crispy_forms.layout import Layout, Field, Div, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import InlineRadios, StrictButton
from crispy_forms.helper import FormHelper


class CustomInviteForm(InviteForm):
    class Meta:
        model = CustomInvitation

# Define the formset using formset_factory
EmailFormSet = formset_factory(CustomInviteForm, extra=1)


# class CustomInviteForm(InviteForm):

#     class Meta:
#         model = CustomInvitation

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # self.fields['phonenumber'].label = "Your Phone Number"
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
        # NOt used as "crispy form" in template was replaced with form|cripsy
        # self.helper.add_input(Submit('submit', 'Submit'))

    # def save(self, email):
    #     return CustomInvitation.create(email=email)
    # @require_POST
    # @csrf_exempt
    # def send_json_invite(request):
    #     if request.method == 'POST':
    #         try:
    #             # Parse JSON data from the request
    #             json_data = json.loads(request.body.decode('utf-8'))

    #             # Check if the JSON data is a list of email objects
    #             if isinstance(json_data, list):
    #                 # Iterate through the list and process each email
    #                 for email_obj in json_data:
    #                     email = email_obj.get('email')
    #                     if email:
    #                         # Process the email, for example, create and send invitations
    #                         # You can use the email variable here
    #                         CustomInvitation.create(email=email)
    #                         response_data = {'message': 'Invitations sent successfully.'}
    #                         status_code = 200
    #                     else:
    #                         response_data = {'message': 'Invalid JSON data format.'}
    #                         status_code = 400
    #         except json.JSONDecodeError:
    #             response_data = {'message': 'Invalid JSON data.'}
    #             status_code = 400

    #         return JsonResponse(response_data, status=status_code)
        
