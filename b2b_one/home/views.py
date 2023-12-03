from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView

# Create your views here.
class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'home/home.html'
    # form_class = PurchaseRequestForm

    def get_template_names(self):
        template_name = 'home/home.html'
        return [template_name]

# Create your views here.
class BootstrapCheat(TemplateView):
    template_name = 'home/cheat.html'
    # form_class = PurchaseRequestForm

    def get_template_names(self):
        template_name = 'home/cheat.html'
        return [template_name]