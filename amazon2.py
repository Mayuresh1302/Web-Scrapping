from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Replace with the URL of the e-commerce site you want to scrape
url = 'https://www.amazon.in/s?k=smartphones+under+50000&crid=1X35Z97P8644&sprefix=%2Caps%2C185&ref=nb_sb_ss_recent_1_0_recent'
driver.get(url)

# Adding a delay to wait for the page to fully load
time.sleep(2)

# Lists to store smartphone names and prices
smartphone_names = []
smartphone_prices = []

# Finding elements containing smartphone names and prices
# Update these XPath or CSS selectors according to the site structure
name_elements = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
price_elements = driver.find_elements(By.XPATH, "//span[@class='a-price-whole']")

# Extracting text from the elements and adding to the lists
for name in name_elements:
    smartphone_names.append(name.text)

for price in price_elements:
    smartphone_prices.append(price.text)

# Printing out the results
for name, price in zip(smartphone_names, smartphone_prices):
    print(f"Smartphone: {name},\n Price: {price}")

# Close the WebDriver
driver.quit()
