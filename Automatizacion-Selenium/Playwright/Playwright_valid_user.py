from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Abre la página de login de Swag Labs
    page.goto('https://www.saucedemo.com/')
    
    # Llenar el campo de usuario con un valor válido
    page.fill('#user-name', 'standard_user')
    
    # Llenar el campo de contraseña con un valor válido
    page.fill('#password', 'secret_sauce')
    
    # Hacer clic en el botón de login
    page.click('#login-button')
    
    # Esperar a que la redirección ocurra y verificar la URL
    page.wait_for_url('https://www.saucedemo.com/inventory.html')
    
    # Verificar si la redirección fue exitosa
    current_url = page.url
    if current_url == 'https://www.saucedemo.com/inventory.html':
        print("La prueba pasó: Redirigido correctamente a la página de inventario.")
    else:
        print("La prueba falló: No se redirigió a la página de inventario.")
    
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
