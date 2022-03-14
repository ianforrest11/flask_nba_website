from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5000/stats_pg"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

print(soup)




