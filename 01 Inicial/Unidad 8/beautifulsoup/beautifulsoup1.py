from bs4 import BeautifulSoup
soup = BeautifulSoup("<!Doctype html><html><head></head><body> <h1>Hola!</h1></body></html>", "html.parser")
soup.prettify()
print(soup.prettify())
