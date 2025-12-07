from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    
    #SELECTORES
    _PRODUCTS = (By.CLASS_NAME,"inventory_item")
    _ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,".inventory_item button")
    _CART = (By.CSS_SELECTOR, ".shopping_cart_badge")
    _NAME_PRODUCTS = (By.CLASS_NAME, "inventory_item_name")
    _CART_PRODUCT = (By.ID, "shopping_cart_container")
    
    #FUNCIONES
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    
    def obtener_todos_los_productos(self):
        self.wait.until(EC.visibility_of_all_elements_located(self._PRODUCTS))
        productos = self.driver.find_elements(*self._PRODUCTS)
        return productos
    
    def obtener_nombres_productos(self):
        productos = self.driver.find_elements(*self._NAME_PRODUCTS)
        return [producto_nombre.text for producto_nombre in productos]
    
    def agregar_primer_producto(self):
        productos = self.wait.until(EC.visibility_of_all_elements_located(self._PRODUCTS))
        
        primer_boton_producto = productos[0].find_element(*self._ADD_TO_CART_BUTTON)
        primer_boton_producto.click()

    def agregar_producto_por_nombre(self,nombre_producto):

        productos = self.driver.find_elements(*self._PRODUCTS)   

        for producto in productos:
            nombre = producto.find_element(*self._NAME_PRODUCTS).text

            if nombre.strip() == nombre_producto.strip():
                boton = producto.find_element(*self._ADD_TO_CART_BUTTON)
                boton.click()
                return self
            
    def carrito_incremento(self):
        return self.wait.until(EC.visibility_of_element_located(self._CART)).text
        
    def ir_al_carrito(self):
        self.driver.find_element(*self._CART_PRODUCT).click()
        
    def validar_producto_añadido(self):
        return self.driver.find_element(*self._NAME_PRODUCTS).text