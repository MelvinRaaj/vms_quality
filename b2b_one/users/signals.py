from allauth.account.signals import user_signed_up
from invitations.utils import get_invitation_model
from .models import Tenant

def user_signed_up(request, user, **kwargs):
    try:
        Invitation = get_invitation_model() ### Get the Invitation model
        # invite = Invitation.objects.get(email=user.inviter) ### Grab the Invitation instance
        companies = Tenant.objects.get(company__user=user.email)
        user.company = Tenant.objects.get(company=companies)
        user.save()
    except Invitation.DoesNotExist:
        print("this was probably not an invited user.")
