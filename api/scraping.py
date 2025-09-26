from playwright.sync_api import sync_playwright
import json
from datetime import datetime

def obtener_cotizaciones():
  datos = {}

  with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=["--disable-dev-shm-usage", "--no-sandbox"] 
    )
    page = browser.new_page()

    ## Cambios Chaco
    try:
        page.goto("https://www.cambioschaco.com.py/en/", timeout=90000)
        page.wait_for_load_state("networkidle", timeout=60000)
        datos["chaco"] = {
            "compra": page.locator("#exchange-usd .purchase").first.inner_text(),
            "venta": page.locator("#exchange-usd .sale").first.inner_text(),
        }
    except Exception as e:
        datos["chaco"] = {"compra": None, "venta": None, "error": str(e)}

     ## M y D
    try:
        page.goto("https://www.mydcambios.com.py/", timeout=90000)
        page.wait_for_load_state("networkidle", timeout=60000)
        datos["myd"] = {
            "compra": page.locator("ul:has(img[src*='us-1.png']) li")
            .nth(1)
            .inner_text(),
            "venta": page.locator("ul:has(img[src*='us-1.png']) li")
            .nth(2)
            .inner_text(),
        }
    except Exception as e:
       datos["myd"] = {"compra": None, "venta": None, "error": str(e)}
          
   

    ## Maxi Cambios
    try:
        page.goto("https://www.maxicambios.com.py/",timeout=90000)
        page.wait_for_load_state("networkidle", timeout=60000)
        tr = page.locator("tr", has_text="DÓLAR")
        datos["maxi"] = {
            "compra": tr.locator("td").nth(1).inner_text(),
            "venta": tr.locator("td").nth(2).inner_text(),
        }       
    except Exception as e:
        datos["maxi"] = {"compra": None, "venta": None, "error": str(e)} 

    ## Cambios FE
    try:
        page.goto("https://www.fecambios.com.py/", timeout=90000)
        page.wait_for_load_state("networkidle", timeout=60000)
        dolar_tr = page.locator("#tasks_vmo_c tr", has_text="USD")
        compra = dolar_tr.locator("td").nth(1).inner_text()
        venta = dolar_tr.locator("td").nth(2).inner_text()
        datos["fe"] = {"compra": compra, "venta": venta}
    except Exception as e:
         datos["fe"] = {"compra": None, "venta": None, "error": str(e)}  


    browser.close()

  datos["ultima_actualizacion"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

  with open("diario.json", "w") as archivo:
      json.dump(datos, archivo, indent=4)

  return datos