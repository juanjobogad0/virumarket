from playwright.sync_api import sync_playwright
import json
from datetime import datetime
import time

def obtener_cotizaciones():
    datos = {}

    def scrapear_and_retry(scraper, reintentos=3):
        for intento in range(reintentos):
            try:
                return scraper()
            except Exception as e:
                if intento == reintentos - 1:
                    return {"compra": None, "venta": None, "error": str(e)}    

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-dev-shm-usage", "--no-sandbox"]
        )
        page = browser.new_page()

        # Bloquear recursos innecesarios
        page.route("**/*", lambda route: route.abort() 
                   if route.request.resource_type in ["image", "stylesheet", "font"] 
                   else route.continue_())

        ## Cambios Chaco
        datos["chaco"] = scrapear_and_retry(lambda: (
            page.goto("https://www.cambioschaco.com.py/en/", timeout=90000),
            page.wait_for_selector("#exchange-usd .purchase", timeout=30000),
           {
                "compra": page.locator("#exchange-usd .purchase").first.inner_text().strip(),
                "venta": page.locator("#exchange-usd .sale").first.inner_text().strip(),
            }
        )[-1]) ### -1 devuleve el ultimo elemento, osea el dicc. 

        time.sleep(1)

        ## M y D
        datos["myd"] = scrapear_and_retry(lambda: (
            page.goto("https://www.mydcambios.com.py/", timeout=90000),
            page.wait_for_selector("ul:has(img[src*='us-1.png']) li:nth-child(2)", timeout=30000),
            {
                "compra": page.locator("ul:has(img[src*='us-1.png']) li").nth(1).inner_text().strip(),
                "venta": page.locator("ul:has(img[src*='us-1.png']) li").nth(2).inner_text().strip(),
            }
        )[-1])

        time.sleep(1)

        ## Maxi Cambios
        datos["maxi"] = scrapear_and_retry(lambda: (
            page.goto("https://www.maxicambios.com.py/", timeout=90000),
            page.wait_for_selector("tr:has-text('DÓLAR') td:nth-child(2)", timeout=30000),
            tr := page.locator("tr", has_text="DÓLAR"),
            {
                "compra": tr.locator("td").nth(1).inner_text().strip(),
                "venta": tr.locator("td").nth(2).inner_text().strip(),
            }   
        )[-1])

        time.sleep(1)
    
        ## Cambios FE
        datos["fe"] = scrapear_and_retry(lambda: (
            page.goto("https://www.fecambios.com.py/", timeout=90000),
            page.wait_for_selector("#tasks_vmo_c tr:has-text('USD') td:nth-child(2)", timeout=30000),
            dolar_tr := page.locator("#tasks_vmo_c tr", has_text="USD"),
             {
                "compra": dolar_tr.locator("td").nth(1).inner_text().strip(),
                "venta": dolar_tr.locator("td").nth(2).inner_text().strip(),
            }

        )[-1])

        time.sleep(1)

        browser.close()

    datos["ultima_actualizacion"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("diario.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    return datos


obtener_cotizaciones()


# def scrape_maxi():
#     page.goto("https://www.maxicambios.com.py/", timeout=90000)
#     page.wait_for_selector("tr:has-text('DÓLAR') td:nth-child(2)", timeout=30000)
#     tr = page.locator("tr", has_text="DÓLAR")
#     return {
#         "compra": tr.locator("td").nth(1).inner_text().strip(),
#         "venta": tr.locator("td").nth(2).inner_text().strip(),
#     }

# datos["maxi"] = scrapear_and_retry(scrape_maxi)