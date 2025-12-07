from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.cart_page import CartPage

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver,usuario,password):
    
    driver = login_in_driver
    cart_page = CartPage(driver)
    
    #agregamos el producto
    cart_page.agregar_primer_producto()
    
    #validamos si se incremento el carrito
    assert cart_page.carrito_incremento() == "1"
    
    #nos dirigimos al carrito
    cart_page.ir_al_carrito()
    
    #validamos si se encuentra el producto en el carrito
    assert cart_page.validar_producto_añadido() == "Sauce Labs Backpack"