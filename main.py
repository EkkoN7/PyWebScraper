import requests
from bs4 import BeautifulSoup
response = requests.get("https://books.toscrape.com/")
html_content = response.text
soup = BeautifulSoup(html_content, "lxml")
print(soup.title)
#print(soup.p)
print(soup.a)

