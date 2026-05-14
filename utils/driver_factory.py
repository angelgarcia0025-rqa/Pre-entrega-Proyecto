from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def crear_driver():
    """Crea y configura el navegador Chrome."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)

    return driver