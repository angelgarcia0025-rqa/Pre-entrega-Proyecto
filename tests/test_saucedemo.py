import os
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import configurar_logger

from utils.driver_factory import crear_driver

URL = "https://www.saucedemo.com/"
USUARIO = "standard_user"
PASSWORD = "secret_sauce"

logger = configurar_logger()


os.makedirs("reports/screenshots", exist_ok=True)
os.makedirs("reports/logs", exist_ok=True)

logging.basicConfig(
    filename="reports/logs/ejecucion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def hacer_login(driver):
    """Realiza login con credenciales válidas."""
    driver.get(URL)

    driver.find_element(By.ID, "user-name").send_keys(USUARIO)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()


def test_login_exitoso(driver):

    logger.info("Inicio del test: login exitoso")
    hacer_login(driver)

    assert "/inventory.html" in driver.current_url
    assert driver.title == "Swag Labs"

    titulo = driver.find_element(By.CSS_SELECTOR, ".title").text
    assert titulo == "Products"

    logging.info("Login exitoso validado correctamente.")
    print("Test OK")


def test_catalogo_productos(driver):
    logger.info("Catálogo de productos validado correctamente")
    hacer_login(driver)

    titulo = driver.find_element(By.CSS_SELECTOR, ".title").text
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    filtro = driver.find_element(By.CLASS_NAME, "product_sort_container")

    assert titulo == "Products"
    assert len(productos) > 0
    assert menu.is_displayed()
    assert filtro.is_displayed()

    primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text

    logging.info(f"Primer producto encontrado: {primer_producto} - {primer_precio}")
    print("Test OK")


def test_agregar_producto_al_carrito(driver):
    logger.info("Productos agregado correctamente")
    hacer_login(driver)

    primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    boton_add_to_cart = driver.find_element(
        By.XPATH,
        "(//button[contains(@id,'add-to-cart')])[1]"
    )
    boton_add_to_cart.click()

    badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert badge.text == "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    assert producto_carrito == primer_producto

    logging.info(f"Producto agregado correctamente al carrito: {producto_carrito}")
    print("Test OK")