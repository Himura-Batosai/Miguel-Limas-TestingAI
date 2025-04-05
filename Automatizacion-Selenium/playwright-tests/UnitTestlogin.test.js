const { test, expect } = require('@playwright/test');

test('Valid login to SauceDemo', async ({ page }) => {
    await page.goto('https://www.saucedemo.com/');
    
    // Llenar el campo de usuario
    await page.fill('#user-name', 'standard_user');
    
    // Llenar el campo de contraseña
    await page.fill('#password', 'secret_sauce');
    
    // Hacer clic en el botón de login
    await page.click('#login-button');
    
    // Esperar a que la página de inventario se cargue
    await page.waitForSelector('.inventory_list');
    
    // Verificar que estamos en la página de inventario
    const currentUrl = page.url();
    expect(currentUrl).toBe('https://www.saucedemo.com/inventory.html');
});
