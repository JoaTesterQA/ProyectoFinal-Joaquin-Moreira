from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class InventoryPage:
    
    #SELECTORES
    _TITLE = (By.CSS_SELECTOR, ".app_logo")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _NOMBRE_PRODUCT = (By.CLASS_NAME, "inventory_item_name ")
    _MENU = (By.ID, "react-burger-menu-btn")
    _FILTRO = (By.CLASS_NAME, "product_sort_container")
    
    #FUNCIONES
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    
    def obtener_titulo(self):
        return self.driver.find_element(*self._TITLE).text
    
    def obtener_producto(self):
        productos =  self.wait.until(EC.visibility_of_all_elements_located(self._PRODUCTS)) 
        primer_producto = productos[0].find_element(*self._NOMBRE_PRODUCT)
        return primer_producto.text
    
    def filtro_menu(self):
        self.driver.find_element(*self._MENU).click()
        
    def chekear_filtro(self):
        filtro = Select(self.driver.find_element(*self._FILTRO))
        filtro.select_by_index(2)