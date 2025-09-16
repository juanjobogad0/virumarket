from django.db import models

# Create your models here.
class CasaDeCambio(models.Model):
  nombre = models.CharField(max_length=255, unique=True)
  url = models.URLField(blank=True, null=True)

  def __str__(self):
     return self.nombre
  
  class Meta:
    db_table = "casas_de_cambio"



class Cotizaciones(models.Model):
    casa = models.ForeignKey(CasaDeCambio, on_delete=models.PROTECT)
    compra = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    venta = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    mensaje_error = models.TextField(null=True, blank=True)


    def __str__(self):
      return f"{self.casa.nombre} - {self.fecha.strftime('%d-%m-%Y %H:%M')}"


    class Meta:
        db_table = "cotizaciones"
        ordering = ["-fecha"]



