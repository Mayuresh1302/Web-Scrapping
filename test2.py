from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Set up the Chrome WebDriver
service = Service(executable_path='chromedriver.exe')  # Update 'path_to_chromedriver' with the path to your ChromeDriver
driver = webdriver.Chrome(service=service)

# Open the Google search link
url = "https://www.google.com/search?q=today+news&rlz=1C1GCEU_enIN1020IN1020&oq=toda&gs_lcrp=EgZjaHJvbWUqBggBEEUYOzIGCAAQRRg5MgYIARBFGDsyCggCEC4YsQMYgAQyDQgDEAAYsQMYyQMYgAQyCggEEAAYkgMYgAQyDQgFEAAYkgMYgAQYigUyDQgGEAAYgwEYsQMYgAQyBggHEEUYPNIBCDI0MjJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"
driver.get(url)

# Wait for the page to load
time.sleep(3)

# Extract the page source
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all link containers
results = soup.find_all('div', class_='g')

# Extract and print links and their sources
for result in results:
    link = result.find('a')['href']
    source = result.find('span').text if result.find('span') else 'Source not found'
    print(f"Link: {link}\nSource: {source}\n")

# Close the browser
driver.quit()
