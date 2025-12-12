import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from datetime import datetime

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox") # github
    options.add_argument("--disable-gpu") # github
    options.add_argument("--window-size=1920,1080") # github
    options.add_argument("--headless=new") # github
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()

@pytest.fixture    
def login_in_driver(driver):
    login = LoginPage(driver)
    login.abrir_pagina()            
    login.login_completo("standard_user", "secret_sauce") 
    return driver                    
    
@pytest.fixture
def url_base():
    return "https://reqres.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres_3665beb867ec4609abbe6ce2d0390655"} 

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    #Captura screenshots automáticamente cuando un test falla
    outcome = yield
    result = outcome.get_result()
    
     # Solo capturar screenshot en la etapa 'call' cuando hay fallo
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver")
        
        if driver:
     # Carpeta donde se guardarán las capturas
            screenshots_dir =Path("screenshots")
            screenshots_dir.mkdir(exist_ok=True)
            
            #nombre del archivo
            test_name = item.name
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = screenshots_dir / f"{test_name}_{timestamp}.png"
            
            driver.save_screenshot(str(filename))
            print(f" Screenshot guardado en: {filename}")