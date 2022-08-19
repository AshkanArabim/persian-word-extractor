from bs4 import BeautifulSoup
import requests

mainPage = requests.get('https://vajehyab.com/')
soup = BeautifulSoup(mainPage.content, 'html.parser')
search = soup.find('input', id = 'q')
print(search)