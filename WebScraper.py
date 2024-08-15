from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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

try:
    # Warte bis zu 10 Sekunden, bis ein bestimmtes Element auf der Seite geladen ist (passe den XPath entsprechend an)
    pdf_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//a[contains(@href, 'viewcontent.cgi')]"))
    )
    for link in pdf_links:
        link.click()  # Auf jeden Link klicken


except TimeoutException:
    print("Das Element wurde nicht innerhalb der angegebenen Zeit gefunden.")

except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

finally:
    driver.quit()
