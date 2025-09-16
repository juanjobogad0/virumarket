from rest_framework import serializers
from .models import Cotizaciones

class CotizacionesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cotizaciones
    fields = '__all__'