from rest_framework import serializers
from .models import Cotizaciones, CasaDeCambio

class CasaDeCambioSerializer(serializers.ModelSerializer):
  class Meta:
    model = CasaDeCambio
    fields = '__all__'


class CotizacionesSerializer(serializers.ModelSerializer):
  casa_cambio = serializers.CharField(source='casa.nombre', read_only=True)
  casa_id = serializers.CharField(source='casa.id', read_only=True)

  class Meta:
    model = Cotizaciones
    fields = [
        "id",
        "compra",
        "venta",
        "fecha",
        "mensaje_error",
        "casa_id",
        "casa_cambio"
    ]