from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import CotizacionesSerializer
from .models import Cotizaciones
from rest_framework import viewsets

class CotizacionesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cotizaciones.objects.all()
    serializer_class = CotizacionesSerializer






