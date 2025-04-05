const { test, expect } = require('@playwright/test');
const { ai } = require('@zerostep/playwright');

test('Invalid login with ZeroStep', async ({ page }) => {
    await page.goto('https://www.saucedemo.com/');
    
    // Llenar el campo de contraseña con un valor inválido
    await ai('Fill the password field with "BadPassword"', { page, test });
    
    // Llenar el campo de usuario con un valor inválido
    await ai('Fill the username field with "Cleo!@#"', { page, test });
    
    // Hacer clic en el botón de login
    await ai('Click the login button', { page, test });
    
    // Esperar a que aparezca el mensaje de error
    const errorMessage = await ai('Wait for the error message to appear', { page, test });
    
    // Verificar si el mensaje de error aparece y que permanezcamos en la página de login
    if (errorMessage) {
        console.log("La prueba pasó: Apareció un mensaje de error.");
        
        // Verificar el mensaje de error específico
        const errorText = await errorMessage.innerText();
        if (errorText === "Epic sadface: Username and password do not match any user in this service") {
            console.log("La prueba pasó: El mensaje de error es correcto.");
        } else {
            console.log("La prueba falló: El mensaje de error no es correcto.");
        }
        
        // Verificar que permanezcamos en la página de login
        const currentUrl = page.url();
        if (currentUrl === 'https://www.saucedemo.com/') {
            console.log("La prueba pasó: Permanecemos en la página de login.");
        } else {
            console.log("La prueba falló: No permanecemos en la página de login.");
        }
    } else {
        console.log("La prueba falló: No apareció un mensaje de error.");
    }
});
