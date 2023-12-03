from django.shortcuts import render, redirect, reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from allauth.account.views import SignupView, LoginView, EmailVerificationSentView
from allauth.account import app_settings, signals


from .models import UserProfile, CustomUser

from.forms import UserProfileForm, CustomUserCreationForm, CustomUserCreationForm_Phone, CustomUserCreationForm_Invite


# External Sign Up
class SignUpViews(SignupView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    # def get_success_url(self):
    #     return reverse("login")
        
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.request = self.request
    #     return form

# External Sign Up
class SignUpViews_Phone(SignupView):
    template_name = 'registration/signup_phone.html'
    form_class = CustomUserCreationForm_Phone


class WhatsAppVerificationSentView(TemplateView):
    template_name = "registration/whatsapp_verification_sent." + app_settings.TEMPLATE_EXTENSION

# External Sign Up
class SignUpViews_Invite(SignupView):
    template_name = 'registration/signup_invite.html'
    form_class = CustomUserCreationForm_Invite

    # def get_success_url(self):
    #     return reverse("login")
        
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     form.request = self.request
    #     return form

# External Sign Up
class SignUpViews_Phone_Invite(SignupView):
    template_name = 'registration/signup_phone_invite.html'
    form_class = CustomUserCreationForm_Phone


#User Profile
class UserProfileView(LoginRequiredMixin, DetailView):
    template_name = 'users/user_details.html'
    context_object_name ='users'
    slug_field = "email"
    slug_url_kwarg = "email"

    def get_queryset(self):
        user = self.request.user

        queryset = UserProfile.objects.filter(email__email=user.email)
        return queryset

#User Update
class UserUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'users/user_update.html'
    context_object_name ='users'
    form_class = UserProfileForm
    slug_field = "email"
    slug_url_kwarg = "email"

    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.filter(email__email=user.email)
        return queryset

    def get_success_url(self):
        user = self.request.user
        return reverse("users:userprofile", args=[user.id])


#user list
class UserListView(LoginRequiredMixin, TemplateView):
    template_name = 'users/user_list.html'
    # context_object_name ='users'
    # model = UserProfile
    # paginate_by = 10

    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = UserProfile.objects.filter(email__email=user.email)
    #     return queryset



