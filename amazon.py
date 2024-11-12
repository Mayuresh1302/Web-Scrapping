from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

url = ("https://www.amazon.in/s?k=smartphones+under+50000&crid=1XTM4CZ39TV7B&sprefix=smartphones+under+50000%2Caps%2C201&ref=nb_sb_noss_1")
driver.get(url)

sleep(3)
soup = BeautifulSoup(driver.page_source, 'html.parser')
products = soup.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')

for i in products:
    print(i.get_text())

driver.quit()