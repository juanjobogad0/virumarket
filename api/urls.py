from django.urls import path, include
from api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'cotizaciones', views.CotizacionesViewSet)

urlpatterns = [
    path("", include(router.urls)), 
]