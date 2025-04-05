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
    
    # Llenar el campo de contraseña con un valor inválido
    password = driver.find_element(By.ID, 'password')
    password.send_keys('BadPassword')
    
    # Llenar el campo de usuario con un valor inválido
    username = driver.find_element(By.ID, 'user-name')
    username.send_keys('Cleo!@#')
    
    # Hacer clic en el botón de login
    login_button = driver.find_element(By.ID, 'login-button')
    login_button.click()
    
    # Esperar a que aparezca el mensaje de error
    error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h3[@data-test="error"]')))
    
    # Verificar si el mensaje de error aparece y que permanezcamos en la página de login
    if error_message:
        print("La prueba pasó: Apareció un mensaje de error.")
        
        # Verificar el mensaje de error específico
        error_text = error_message.text
        if error_text == "Epic sadface: Username and password do not match any user in this service":
            print("La prueba pasó: El mensaje de error es correcto.")
        else:
            print("La prueba falló: El mensaje de error no es correcto.")
        
        # Verificar que permanezcamos en la página de login
        current_url = driver.current_url
        if current_url == 'https://www.saucedemo.com/':
            print("La prueba pasó: Permanecemos en la página de login.")
        else:
            print("La prueba falló: No permanecemos en la página de login.")
    else:
        print("La prueba falló: No apareció un mensaje de error.")
    
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    driver.quit()
