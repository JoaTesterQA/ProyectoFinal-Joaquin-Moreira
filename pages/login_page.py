from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://www.saucedemo.com/"
    
    #SELECTORES
    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_INPUT = (By.ID, "login-button")
    
    #FUNCIONES
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    
    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self
    
    def completar_usuario(self, usuario):
        campo = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        campo.send_keys(usuario)
        return self
    
    def completar_contraseña(self, contraseña):
        campo = self.driver.find_element(*self._PASS_INPUT)
        campo.send_keys(contraseña)
        return self
    
    def click_login(self):
        self.driver.find_element(*self._LOGIN_INPUT).click()
        
    def login_completo(self, usuario, contraseña):
        self.completar_usuario(usuario)
        self.completar_contraseña(contraseña)
        self.click_login()
        return self
    
    def mensaje_error(self):
        div_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container.error h3")))
        return div_error.text