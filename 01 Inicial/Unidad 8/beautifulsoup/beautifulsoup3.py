import requests
from bs4 import BeautifulSoup



data = requests.get("http://localhost/beautifulsoup_php/recuperar_beautifulsoap.php")
print(data)
soup = BeautifulSoup(data.text, "html.parser")
print(soup.find('a',{'class':'estiloAncla'}))
