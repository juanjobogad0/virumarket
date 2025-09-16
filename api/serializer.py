from rest_framework import serializers
from .models import Cotizaciones, CasaDeCambio

class CasaDeCambioSerializer(serializers.ModelSerializer):
  class Meta:
    model = CasaDeCambio
    fields = '__all__'


class CotizacionesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cotizaciones
    fields = '__all__'