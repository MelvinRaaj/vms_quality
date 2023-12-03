from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required


from .views import UserProfileView, UserUpdateView
from .tables import UserListTable

app_name= "users"

urlpatterns = [

    path('<str:email>/', UserProfileView.as_view(), name='userprofile' ),
    path('<str:email>/update/', UserUpdateView.as_view(), name='userprofileupdate' ),
    path('list/', login_required(UserListTable.as_view()), name='user_lists_table' ),

]
