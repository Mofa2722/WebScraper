from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#Configure Chrome options
options = Options()
options.add_argument("--headless")

#Set path to the Chrome Driver
DRIVER_PATH = (r"C:\Users\Hamudi\PycharmProjects\chromedriver-win64\chromedriver.exe")

#Initialize the Chrome Driver
driver = webdriver.Chrome(options)

# Navigate to the URL
driver.get("https://news.ycombinator.com/")

# locate the first 'a' of the first 'p', wich locates the article title and link
title_element = driver.find_element(By.XPATH, '//tr[@class="athing"]/td[3]/span[@class="titleline"]/a')

# get the href attribute wich contains the link
link = title_element.get_attribute('href')

# Output the page source to the console
print(title_element.click())

# print current URL after clicking
print(driver.current_url)

# It's a good practice to close the browser when done
driver.quit()

#speichern in datei
# python .\Versuch_1.py > output.txt