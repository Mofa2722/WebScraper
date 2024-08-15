from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

options.add_experimental_option('prefs',
{"download.default_directory": r"C:\Users\Hamudi\PycharmProjects\pythonProject\PDF",
        "download.promt_for_download": False, "plugins.always_open_pdf_externally": True})

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

URL = 'https://aisel.aisnet.org/wi2023'
driver.get(URL)

#tutorial zeigt folgendes
driver.maximize_window()
driver.implicitly_wait(3)

# aus video geschrieben mit pfad aus WI seite
cookie_div = driver.find_element(By.XPATH,'//div[@id="onetrust-button-group"]')
if cookie_div: driver.find_element(By.XPATH, '//div[@id="onetrust-button-group"]//button[text()="Akzeptiere alle Cookies"]').click()

# It's a good practice to close the browser when done
driver.quit()