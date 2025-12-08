# Proyecto de pruebas automatizadas de la web SAUCE DEMO

## herramientas que se utilizo:
- Python 3.13.5
- Pytest 8.4.1
- Selenium 4.34.0
- WebDriver 4.0.2
- Logging
- Request
- CSV/JSON

## Resumen del proyecto:
- Resumen del proyecto.
Este proyecto consiste en la **automatización de pruebas funcionales** sobre la página [Sauce Demo](https://www.saucedemo.com/). 
Aplicando el modelo Page Object Model, logging, APIs, reportes html, captura de pantalla y manejo de dato externos.
El objetivo principal es verificar el **flujo completo de usuario**, incluyendo:
- Inicio de sesión exitoso.
- Visualización de productos.
- Aplicación de filtros.
- Adición de productos al carrito.
- Validación de elementos dentro del carrito.
- Manejo de APIs.


## Estructura del proyecto:
- Login exitoso y fallido
- Comportamiento de la pagina de inventario
- Comportamiento de la pagina del carrito
- API (Reqres): GET users, POST create user, DELETE user, validaciones de codigos HTTP, validaciones de estructura JSON

## Reportes y logs
- En cada ejecución de los tests genera automaticamente los resultados en **report html**, **log**, **captura de pantalla**

## Reporte HTML
- Se genera el reporte en la raiz del proyecto como **report.html**

## Captura de pantalla
- Se genera si un test falla, se encuentra en la carpeta **screenshots**

## Logs de ejecucion
- Se muestra la informacion detallada de cada ejecución de los tests se ubica en la carpeta logs/suite.log

## Datos de prueba
- datos/data_login.csv -> aca se encuentra los datos del login true/false
- datos/productos.json -> se encuentra 3 productos en formato json. seleccionados de  la web SAUCE DEMO
## Como correr las pruebas:
- Clonar repositorio:
git clone https://github.com/JoaTesterQA/ProyectoFinal-Joaquin-Moreira.git
- instalar dependencias:
pip install -r requirements.txt
- Nos dirigimos al archivo run_test.py y lo corremos desde el run python.


