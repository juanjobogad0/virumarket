from django.core.management.base import BaseCommand
from api.scraping import obtener_cotizaciones  
from api.models import Cotizaciones, CasaDeCambio
import psutil, os
import psutil

class Command(BaseCommand):
    help = "Obtiene las cotizaciones"

    def handle(self, *args, **kwargs):
        try:
          datos = obtener_cotizaciones()

          for casa, valores in datos.items():
              if casa == "ultima_actualizacion":
                  continue
              mensaje_error = None 
              try:
                compra=valores["compra"].replace(".", "").replace(",", ".")
                venta=valores["venta"].replace(".", "").replace(",", ".")
              except Exception as e:
                compra = None
                venta = None
                mensaje_error = str(e)
                self.stdout.write(self.style.ERROR(f"{casa} -> {mensaje_error}"))
              
              casa_obj, _ = CasaDeCambio.objects.get_or_create(nombre=casa)
              
              Cotizaciones.objects.create(
                  casa=casa_obj,
                  compra=compra,
                  venta=venta,
                  mensaje_error=mensaje_error                
              )
            
              self.stdout.write(self.style.SUCCESS("Cotizaciones guardadas con éxito"))

        finally:
            for proceso in psutil.process_iter(["pid", "name"]):
                if "chrome" in proceso.info["name"].lower():
                    proceso.kill()       

            print("Memoria usada:", psutil.virtual_memory().percent)
            print("CPU usada:", psutil.cpu_percent())   

        




