from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import CotizacionesSerializer, CasaDeCambioSerializer
from .models import Cotizaciones, CasaDeCambio
from rest_framework import viewsets

class CasasViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CasaDeCambio.objects.all()
    serializer_class = CasaDeCambioSerializer


class CotizacionesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cotizaciones.objects.all()
    serializer_class = CotizacionesSerializer






