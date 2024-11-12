import requests
from bs4 import BeautifulSoup

# The provided Google search URL
url = "https://www.google.com/search?q=today+news&rlz=1C1GCEU_enIN1020IN1020&oq=toda&gs_lcrp=EgZjaHJvbWUqBggBEEUYOzIGCAAQRRg5MgYIARBFGDsyCggCEC4YsQMYgAQyDQgDEAAYsQMYyQMYgAQyCggEEAAYkgMYgAQyDQgFEAAYkgMYgAQYigUyDQgGEAAYgwEYsQMYgAQyBggHEEUYPNIBCDI0MjJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8"

# Headers to mimic a request from a real browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send a GET request to the URL
response = requests.get(url, headers=headers)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all links on the page
# links = soup.find_all("a")
# source = soup.find_all("span")
article = soup.find_all('h3','span')

# Extract and print only the links (href attributes)
for link in article:
    links = soup.find_all("h3")
    source = soup.find_all("span")
    href = links.get("href")
    print(links, source)

