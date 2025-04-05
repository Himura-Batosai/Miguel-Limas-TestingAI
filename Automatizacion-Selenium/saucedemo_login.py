from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Ruta al WebDriver descargado
driver_path = 'C:\\Users\\MLimas\\OneDrive - Epicor\\Documents\\QA Minds\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)

# Configurar opciones de Chrome
chrome_options = Options()
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument('--disable-gpu')

try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Abre la página de login de Swag Labs
    driver.get('https://www.saucedemo.com/')
    
    # Espera a que la página se cargue completamente
    time.sleep(5)
    
    # Llenar el campo de usuario
    username = driver.find_element(By.ID, 'user-name')
    username.send_keys('standard_user')
    
    # Llenar el campo de contraseña
    password = driver.find_element(By.ID, 'password')
    password.send_keys('secret_sauce')
    
    # Hacer clic en el botón de login
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    
    # Esperar a que la redirección ocurra y verificar la URL
    WebDriverWait(driver, 10).until(EC.url_to_be('https://www.saucedemo.com/inventory.html'))
    
    # Verificar si la redirección fue exitosa
    current_url = driver.current_url
    if current_url == 'https://www.saucedemo.com/inventory.html':
        print("La prueba pasó: Redirigido correctamente a la página de inventario.")
    else:
        print("La prueba falló: No se redirigió a la página de inventario.")
    
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    driver.quit()
