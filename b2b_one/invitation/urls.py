from django.contrib import admin
from django.urls import path, re_path

from .views import CustomInvite, CustomAcceptInvite

app_name= "invitation"

urlpatterns = [

    path('', CustomInvite.as_view(), name='user-invite'),
    re_path(
        r"^accept-invite/(?P<key>\w+)/?$",
        CustomAcceptInvite.as_view(),
        name="accept-invite",
    ),
]
