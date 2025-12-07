import pytest

from utils.datos import leer_csv_login
from pages.login_page import LoginPage
from utils.logger import logger

@pytest.mark.parametrize("usuario,password,debe_funcionar",leer_csv_login("datos/data_login.csv"))
def test_login_validation(login_in_driver, usuario, password, debe_funcionar):
    logger.info("completando los datos del usuario")
    driver = login_in_driver
    
    login_page = LoginPage(driver)
    login_page.abrir_pagina().login_completo(usuario, password)

    #validamos si ingresamos datos validos nos redirige a la pagina
    if debe_funcionar:
        assert "/inventory.html" in login_page.driver.current_url, "No se dirigió a la página"
    else:
        mensaje_error = login_page.mensaje_error()
        assert "Epic sadface" in mensaje_error, "No se muestra el mensaje de error"
