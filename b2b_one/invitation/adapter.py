from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from invitations.adapters import BaseInvitationsAdapter

from invitations.utils import get_invitation_model

from allauth.account import app_settings, signals

from django.contrib.sites.shortcuts import get_current_site

from users.forms import CustomUser

from tenant.models import Tenant

from twilio.rest import Client

account = "AC20e86fe43dfb911b90bdf13f37232527"
token = "a5e10d690e7a0b4b4856af0681b2ba25"
client = Client(account, token)


class InviteAdapter(BaseInvitationsAdapter):

    def send_invitation(self, request, invitation):
        # Custom send_invitation logic here
        # ...
        return super().send_invitation(request, invitation)