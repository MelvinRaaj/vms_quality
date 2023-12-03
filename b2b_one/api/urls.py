from django.urls import include, path
from rest_framework import routers
from .views import UserViewApi, TenantViewApi
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

app_name= "api"

router = routers.DefaultRouter()
router.register(r"user", UserViewApi)
router.register(r"tenant", TenantViewApi)

urlpatterns = [
    path("", include(router.urls)),
    
]