from django.shortcuts import render, redirect, reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

from allauth.account.views import SignupView, LoginView
from .models import Tenant

# Create your views here.

#Tenant Profile
class TenantView(LoginRequiredMixin, DetailView):
    template_name = 'tenant/tenant_details.html'
    context_object_name ='tenant'
    slug_field = "company"
    slug_url_kwarg = "company"

    def get_queryset(self):
        user = self.request.user

        queryset = Tenant.objects.filter(company=user.company)
        return queryset

# #User Update
# class UserUpdateView(LoginRequiredMixin, UpdateView):

#     template_name = 'users/user_update.html'
#     context_object_name ='users'
#     form_class = UserProfileForm
#     slug_field = "email"
#     slug_url_kwarg = "email"

#     def get_queryset(self):
#         user = self.request.user
#         queryset = UserProfile.objects.filter(email__email=user.email)
#         return queryset

#     def get_success_url(self):
#         user = self.request.user
#         return reverse("users:userprofile", args=[user.id])