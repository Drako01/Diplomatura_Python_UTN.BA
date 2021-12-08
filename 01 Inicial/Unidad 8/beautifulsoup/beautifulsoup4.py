import requests
from bs4 import BeautifulSoup
data2 = requests.get("http://localhost/beautifulsoup_php/recuperar_beautifulsoap2.php?variable1=hola1&variable2=hola2")
soup2 = BeautifulSoup(data2.text, "html.parser")
print(soup2)


"""
http://localhost/beautifulsoup_php/recuperar_beautifulsoap2.php?
variable1=hola1&variable2=hola2
"""
