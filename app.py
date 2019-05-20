from bs4 import BeautifulSoup
import requests

link = input()
r = requests.get(link)
soup = BeautifulSoup(r.text)

print(soup.title.get_text())
for p in soup.find_all('p', class_='css-18icg9x evys1bk0'):
    print(p.get_text())