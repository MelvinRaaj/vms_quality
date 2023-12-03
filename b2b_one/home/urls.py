from django.contrib import admin
from django.urls import path

from .views import HomeView, BootstrapCheat

app_name= "home"

urlpatterns = [

    path('home', HomeView.as_view(), name="home_page"),
    path('cheat', BootstrapCheat.as_view(), name="home_cheat"),
]
