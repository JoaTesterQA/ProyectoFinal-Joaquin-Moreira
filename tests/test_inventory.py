from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from pages.inventory_page import InventoryPage
from utils.logger import logger

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_inventory(login_in_driver, usuario, password):
    

    driver = login_in_driver
    inventory_page = InventoryPage(driver)
    
    #validamos el titulo   
    logger.info("Validamos el titulo de la pagina")
    assert inventory_page.obtener_titulo() == "Swag Labs"
    
    #obtenemos el primer producto   
    logger.info("Seleccionamos el primer producto")
    producto = inventory_page.obtener_producto()
    assert producto != ""
    print(f"primer producto: ",producto)
    
    #click en el menu 
    logger.info("filtro del menu")
    inventory_page.filtro_menu()
    
    #click en el filtro   
    logger.info("Seleccioanmos el filtro")
    inventory_page.chekear_filtro()
        