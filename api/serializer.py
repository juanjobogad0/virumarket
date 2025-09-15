from rest_framework import serializer
from .models import Cotizaciones

class CotizacionesSerializer(serializer.ModelSerializer):
  class Meta:
    model = Cotizaciones
    fields = '__all__'