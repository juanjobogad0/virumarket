from playwright.sync_api import sync_playwright
import json
from datetime import datetime
import time

def obtener_cotizaciones():
    datos = {}

    def scrapear_and_retry(scraper, browser, reintentos=2):
        for intento in range(reintentos):
            context = None
            page = None
            inicio = time.perf_counter()
            try:
                context = browser.new_context()                
                page = context.new_page()

                # Bloquear recursos innecesarios
                page.route("**/*", lambda route: route.abort() 
                        if route.request.resource_type in ["image", "stylesheet", "font", "media"] 
                        else route.continue_())
                
                result = scraper(page)
        
                duracion = time.perf_counter() - inicio
                print(f"{scraper.__name__} completado en {duracion:.2f} segundos")
                
                return result

            except Exception as e:                       
                if intento == reintentos - 1:
                    duracion = time.perf_counter() - inicio
                    print(f"{scraper.__name__} falló en {duracion:.2f} segundos {e}")
                    return {"compra": None, "venta": None, "error": str(e)}
                time.sleep(4) 

            finally:
                if page:
                    page.close()
                if context:
                    context.close()

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-dev-shm-usage", "--no-sandbox", "--disable-gpu", "--no-zygote"]
        )                    
    
        def scrape_chaco(page):
            page.goto("https://www.cambioschaco.com.py/en/", timeout=30000)
            page.wait_for_selector("#exchange-usd .purchase", timeout=30000)
            return {
                    "compra": page.locator("#exchange-usd .purchase").first.inner_text().strip(),
                    "venta": page.locator("#exchange-usd .sale").first.inner_text().strip(),
                    }
        datos["chaco"] = scrapear_and_retry(scrape_chaco, browser)  
        
        def scrape_myd(page):
            page.goto("https://www.mydcambios.com.py/", timeout=30000)
            page.wait_for_selector("ul:has(img[src*='us-1.png']) li:nth-child(2)", timeout=30000)
            return {
                "compra": page.locator("ul:has(img[src*='us-1.png']) li").nth(1).inner_text().strip(),
                "venta": page.locator("ul:has(img[src*='us-1.png']) li").nth(2).inner_text().strip(),
            }
        datos["myd"] = scrapear_and_retry(scrape_myd, browser)
        
        def scrape_maxi(page):
            page.goto("https://www.maxicambios.com.py/", wait_until="domcontentloaded", timeout=60000)
            page.wait_for_selector("tr:has-text('DÓLAR') td:nth-child(2)", timeout=30000)
            tr = page.locator("tr", has_text="DÓLAR")
            return {
            "compra": tr.locator("td").nth(1).inner_text().strip(),
            "venta": tr.locator("td").nth(2).inner_text().strip(),
            }
        datos["maxi"] = scrapear_and_retry(scrape_maxi, browser) 
        

        def scrape_fe(page):
                page.goto("https://www.fecambios.com.py/", timeout=30000)
                page.wait_for_selector("#tasks_vmo_c tr:has-text('USD') td:nth-child(2)", timeout=30000)
                dolar_tr = page.locator("#tasks_vmo_c tr", has_text="USD")            
                return {
                    "compra": dolar_tr.locator("td").nth(1).inner_text().strip(),
                    "venta": dolar_tr.locator("td").nth(2).inner_text().strip(),
                }
        datos["fe"] = scrapear_and_retry(scrape_fe, browser)         
               
        browser.close()

    datos["ultima_actualizacion"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("diario.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

    return datos






