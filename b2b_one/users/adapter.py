from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from allauth.account.adapter import DefaultAccountAdapter,get_adapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.utils import (
    build_absolute_uri,
    email_address_exists,
    generate_unique_username,
    get_user_model,
    import_attribute,
)
from allauth.account.signals import user_signed_up
from invitations.utils import get_invitation_model

from allauth.account import app_settings, signals

from django.contrib.sites.shortcuts import get_current_site

from users.forms import CustomUser

from tenant.models import Tenant

from invitation.models import CustomInvitation

from twilio.rest import Client

account = "AC20e86fe43dfb911b90bdf13f37232527"
token = "a5e10d690e7a0b4b4856af0681b2ba25"
client = Client(account, token)


class UserAccountAdapter(DefaultAccountAdapter):
    
    def save_user(self, request, user, form, commit=True):
        """
        This is called when saving user via allauth registration.
        We override this to set additional data on user object.
        """
        # Do not persist the user yet so we pass commit=False
        # (last argument)
        user = super(UserAccountAdapter, self).save_user(request, user, form, commit=False)
        emails = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phonenumber')
        company_name = form.cleaned_data.get('company_name')

        invitation = CustomInvitation.objects.filter(email__iexact=emails).first()
        
        try:
            tenant =Tenant.objects.get(company=company_name)  
        except Tenant.DoesNotExist:
            # emails = None
            pass
        
        # first check is if invited (meaning must have a tenant)
        if invitation:
            company_name = invitation.inviter.company
        # 2nd check is if there is a tenant existing (meaning this is a sign up either phone or email)
        elif Tenant.DoesNotExist :
            company_name = form.cleaned_data.get('company_name')
            Tenant.objects.create(company=form.cleaned_data['company_name'], subdomain_prefix=form.cleaned_data['company_name'])
            user.is_owner =True
        # 3rd check is if the signup/invite is via phone or email , if not phone starts first
        if emails == 'phone_signup@mail.com':
            emails = str(phone)+'@'+'example.com'
            user.sign_up = 'WhatsApp'
            user.phone = phone
            user.username = phone
        else:
            user.username = emails
        user.email = emails
        user.company = Tenant.objects.get(company=company_name)        
        user.save()
        return user

    #got this from chatgpt - this is to send whatsapp or email
    def send_confirmation_mail(self, request, emailconfirmation, signup):
            # Check user sign-up data
            user = emailconfirmation.email_address.user
            print(user)
            url = reverse("account_confirm_email", args=[emailconfirmation.key])
            ############ hack here as it does not support localhost 127 bla bla - when in development use the line below. ########
            # ret = build_absolute_uri(request, url)
            ret = 'www.example.com' + url
             # Send whatsapp instead of email
            if user.sign_up == 'WhatsApp':
                message = client.messages.create( 
                    from_='whatsapp:+14155238886',  
                    body=(f"{'Your SalesMinded signup url code is'} {ret}"),
                    to='whatsapp:'+ user.phone 
                ) 
                return redirect('account_login')
            else:
                # Send a custom confirmation email
                super().send_confirmation_mail(request, emailconfirmation, signup)

    # Change email/whatsapp sent templates after signup
    def respond_email_verification_sent(self, request, user):
        if user.sign_up == 'WhatsApp':
            # do something
            get_adapter(self.request).add_message(
                self.request,
                messages.INFO,
                "account/messages/whatsapp_confirmation_sent.txt",
                {"email": user.phone},
            )
            return HttpResponseRedirect(reverse("account_whatsapp_verification_sent"))
        else:
            # do something else
            return super().respond_email_verification_sent(request, user)
    




        

