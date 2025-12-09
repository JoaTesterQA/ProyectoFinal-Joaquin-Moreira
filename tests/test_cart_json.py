from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.lector_json import leer_json_productos

import time
RUTA_JSON = "datos/productos.json"
from utils.logger import logger

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
@pytest.mark.parametrize("nombre_producto",leer_json_productos(RUTA_JSON))
def test_cart_json(login_in_driver,usuario,password,nombre_producto):
    
    driver = login_in_driver
    cart_page = CartPage(driver)
    # Agregar al carrito el producto
    logger.info(f"Agregamos productos por su nombre: {nombre_producto}")
    cart_page.agregar_producto_por_nombre(nombre_producto)

    # Abrir el carrito
    cart_page.ir_al_carrito()

    time.sleep(1)

    # Validar el producto
    cart_page = CartPage(driver)

    assert cart_page.validar_producto_añadido() == nombre_producto
        