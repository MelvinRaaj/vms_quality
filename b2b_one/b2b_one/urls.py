"""b2b_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from users.views import SignUpViews, SignUpViews_Phone, WhatsAppVerificationSentView, SignUpViews_Invite


urlpatterns = [

    path('admin/', admin.site.urls),
    
    # allauth
    path('accounts/', include('allauth.urls')),

    #api
    path('api', include('api.urls', namespace="api")),

    # YOUR PATTERNS (SWAGGER)
    path('api/schema/', login_required(SpectacularAPIView.as_view()), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    #landing
    path('', include('landing.urls', namespace="landing")),

    #home
    path('', include('home.urls', namespace="home")),

    #users
    path('users', include('users.urls', namespace="users")),
    path('invitation', include('invitation.urls', namespace="invitation")),
    path("invitations/", include('invitations.urls', namespace='invitations')),

    #users
    path('tenant', include('tenant.urls', namespace="tenant")),

    #department
    path('department', include('department.urls', namespace="department")),

    #product_collections
    path('product_collections', include('product_collections.urls', namespace="product_collections")),

    #demo
    path('demo', include('demo.urls', namespace="demo")),

    #quality
    path('quality', include('quality.urls', namespace="quality")),

    #quality2
    path('quality2', include('quality2.urls', namespace="quality2")),

    #products
    path('products', include('products.urls', namespace="products")),

    #shopping_list
    path('shopping_list', include('shopping_list.urls', namespace="shopping_list")),

    #materials
    path('materials', include('materials.urls', namespace="materials")),

    #Rfi
    path('rfi', include('rfi.urls', namespace="rfi")),

    #samples
    path('samples', include('samples.urls', namespace="samples")),

    #design_spec
    # path('design_spec', include('design_spec.urls', namespace="design_spec")),

    # # # Login and User Registration pages
    # path('login', LoginView.as_view(), name="login"),
    # path('reset', PasswordResetView.as_view(), name="reset"),
    # # path('reset-done', PasswordResetDoneView.as_view(), name="password_reset_done"),
    # # path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # # path('password_reset_complete', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # # path('logout', LogoutView.as_view(), name="logout"),
    path('signup', SignUpViews.as_view(), name="signup"),
    path('signup_invite', SignUpViews_Invite.as_view(), name="signup_invite"),
    path('signup_phone', SignUpViews_Phone.as_view(), name="signup_phone"),
    path('confirm-whatsapp/', WhatsAppVerificationSentView.as_view(), name='account_whatsapp_verification_sent'),

]
