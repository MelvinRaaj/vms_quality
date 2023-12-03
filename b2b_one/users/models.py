
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import Permission

import uuid

from .managers import CustomUserManager

from tenant.models import Tenant
# from department.models import Department


# Create your models here.

#MAIN USER class
class CustomUser(AbstractUser):

    username = models.CharField(max_length=300,null=True, blank=True, unique=True)
    last_name = None
    email = models.EmailField(_('email address'), null=True, blank=True, unique=True)
    phone = PhoneNumberField(null=True,blank=True, unique=True)
    is_internal = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    USER_ROLES = (
        ('Management', 'Management'),
        ('Finance', 'Finance'),
        ('Purchasor', 'Purchasor'),
        ('Requestor', 'Requestor'),
        ('Shipper', 'Shipper'),
        ('Quality Manager', 'Quality Manager'),
        ('Quality User', 'Quality User'),
        ('Vendor', 'Vendor'),
    )

    user_role = models.CharField(max_length=300, choices=USER_ROLES, default='Management')
    company = models.ForeignKey(Tenant,related_name='tenant',on_delete=models.CASCADE, blank=True, null=True )

    USER_Sign_Up = (
        ('Email', 'Email'),
        ('WhatsApp', 'WhatsApp'),
    )

    sign_up = models.CharField(max_length=300, choices=USER_Sign_Up, default='Email')

    permission = models.ManyToManyField(Permission, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email} {self.phone}'


### did not implement signal to create new tenant if tenant does not exist and assign tenant to custom user
# signal to create account when new user is created

def post_CustomUser_created_signal(sender, instance, created, **kwargs):
    
    # company_name = instance.company_name
    # try:
    #     tenant = Tenant.objects.get(company=company_name)
    # except Tenant.DoesNotExist:
    #     tenant = None
    
    # if not tenant:
    #     Tenant.objects.create(company=company_name, subdomain_prefix=company_name)

    if created and instance.is_internal == False:
        UserProfile.objects.create(email=instance)

post_save.connect(post_CustomUser_created_signal, sender=CustomUser)


# # user Profiles ( both internal and external users)
class UserProfile(models.Model):

    EMPLOYMENT_STATUS = (
        ('Retired', 'Retired'),
        ('Resigned', 'Resigned'),
        ('Active', 'Active'),
    )

    email= models.ForeignKey(CustomUser,related_name='mainemail',on_delete=models.CASCADE,null=True )
    user_first_name = models.CharField(max_length=300)
    user_last_name = models.CharField(max_length=300)
    user_position = models.CharField(max_length=300,null=True)
    user_birthdate = models.DateField(null=True, blank=True)
    user_id = models.CharField(max_length=300)
    user_facebook = models.CharField(max_length=300)
    user_linkedin = models.CharField(max_length=300)
    user_phone = PhoneNumberField(blank=True)
    user_status = models.CharField(max_length=300, choices=EMPLOYMENT_STATUS)
    


    def __str__(self):
        return str(self.email)
