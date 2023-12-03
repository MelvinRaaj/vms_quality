from django.contrib import admin
from django.urls import path

from .views import LandingPageView, FeaturesPageView, NewsPageView

app_name= "landing"

urlpatterns = [

    path('', LandingPageView.as_view(), name="landing_page"),

    # features page
    path('features', FeaturesPageView.as_view(), name="features"),

    # news page
    path('news', NewsPageView.as_view(), name="news"),

]
