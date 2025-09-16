from django.db import models

# Create your models here.

class Cotizaciones(models.Model):
    casa_de_cambio = models.CharField(max_length=255, unique=True)
    compra = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    venta = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)


    def __str__(self):
      return f"{self.casa_de_cambio} - {self.fecha.strftime('%d-%m-%Y %H:%M')}"


    class Meta:
        db_table = "cotizaciones"
        ordering = ["-fecha"]



