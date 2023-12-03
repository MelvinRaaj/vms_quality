from django.db import models

import datetime
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils import timezone
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

from invitations.app_settings import app_settings
from invitations.base_invitation import AbstractBaseInvitation
from invitations.adapters import get_invitations_adapter
from django.utils.crypto import get_random_string
from invitations import signals
from users.models import CustomUser


# Create your models here.
class CustomInvitation(AbstractBaseInvitation):

    phone = models.CharField(max_length=300,null=True, blank=True, unique=True)
    email = models.EmailField(
        unique=True,
        null=True, 
        blank=True, 
        verbose_name=_("e-mail address"),
        max_length=app_settings.EMAIL_MAX_LENGTH,
    )
    created = models.DateTimeField(verbose_name=_("created"), default=timezone.now)

    @classmethod
    def create(cls, email, inviter=None, **kwargs):
        key = get_random_string(64).lower()
        instance = cls._default_manager.create(
            email=email, key=key, inviter=inviter, **kwargs
        )
        return instance

    def key_expired(self):
        expiration_date = self.sent + datetime.timedelta(
            days=app_settings.INVITATION_EXPIRY,
        )
        return expiration_date <= timezone.now()

    def send_invitation(self, request, **kwargs):
        current_site = get_current_site(request)
        invite_url = reverse(app_settings.CONFIRMATION_URL_NAME, args=[self.key])
        invite_url = request.build_absolute_uri(invite_url)
        ctx = kwargs
        ctx.update(
            {
                "invite_url": invite_url,
                "site_name": current_site.name,
                "email": self.email,
                "key": self.key,
                "inviter": self.inviter,
                #added company as tenant in the email
                "company": self.inviter.company,
            },
        )
        print(ctx)

        email_template = "invitations/email/email_invite"

        get_invitations_adapter().send_mail(email_template, self.email, ctx)
        self.sent = timezone.now()
        self.save()

        signals.invite_url_sent.send(
            sender=self.__class__,
            instance=self,
            invite_url_sent=invite_url,
            inviter=self.inviter,
            company=self.inviter.company
        )

    def __str__(self):
        return f"Invite: {self.email}"
