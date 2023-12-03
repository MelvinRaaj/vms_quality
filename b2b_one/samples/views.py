# views.py
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect, render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.views import View
from django.apps import apps
from django.http import JsonResponse


#import messages
from django.contrib import messages

#import loginrequired
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from .models import ProductCollection, Products

from django.forms import inlineformset_factory

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction

from rfi.models import VendorSamplesResponse


from shopping_list.models import ShoppingList, ShoppingListItem, SL_Samples
from tenant.models import Tenant

# Create your views here.
# this is the baseContextView which should be inherited by all views in app apps (reusable apps)
class BaseAppContextView(View,LoginRequiredMixin):
    def get_app_name(self):
        # Get the app name from the current view's app
        current_app = self.request.resolver_match.app_name
        app_label = apps.get_app_config(current_app).verbose_name
        return app_label

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = self.get_app_name()
        return context
    
class RFISamplesView(BaseAppContextView, ListView, LoginRequiredMixin):
    model = VendorSamplesResponse
    template_name = "samples/samples_list.html"
    context_object_name = "products"