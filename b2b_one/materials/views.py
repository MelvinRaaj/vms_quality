# views.py
from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.views import View
from django.apps import apps
from django.http import JsonResponse

#import messages
from django.contrib import messages

#import loginrequired
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.forms import inlineformset_factory

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Materials

from .forms import Material_Form

from django.db import transaction

# template view
from django.views.generic import TemplateView

# this is the baseContextView which should be inherited by all views in app apps (reusable apps)
class BaseAppContextView(View):
    def get_app_name(self):
        # Get the app name from the current view's app
        current_app = self.request.resolver_match.app_name
        app_label = apps.get_app_config(current_app).verbose_name
        return app_label

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['app_name'] = self.get_app_name()
        return context

class MaterialsView(BaseAppContextView, ListView):
    model = Materials
    template_name = "materials/materials_list.html"
    context_object_name = "products"

# create view for materials
class MaterialCreateView(LoginRequiredMixin,CreateView,BaseAppContextView): 
    model = Materials
    form_class = Material_Form
    template_name = "materials/materials_create_or_update.html"
    success_url = "/materials"

    def form_valid(self, form):
        return super().form_valid(form)
    
# update view for materials
class MaterialUpdateView(LoginRequiredMixin,UpdateView,BaseAppContextView): 
    model = Materials
    form_class = Material_Form
    template_name = "materials/materials_create_or_update.html"
    success_url = "/materials"

    def form_valid(self, form):
        return super().form_valid(form)
    
# delete view for materials
class MaterialDeleteView(LoginRequiredMixin,DeleteView,BaseAppContextView): 
    model = Materials
    template_name = "materials/material_delete.html"
    success_url = "/materials"

    def form_valid(self, form):
        return super().form_valid(form)