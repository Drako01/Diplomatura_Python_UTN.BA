from bs4 import BeautifulSoup

documento_html="""
<!Doctype html><html><head><title>Recorrer Documento html</title></head>
<body>
<p class ="titulo"><b>Título de la historia</b></p>
<p class = "contenido">Contenido de la historia
<a href="ruta 1" class = "estiloAncla" id="link1"> historia 1</a>
<a href="ruta 1" class = "estiloAncla" id="link2"> historia 2</a>
<a href="ruta 1" class = "estiloAncla" id="link3"> historia 3</a>
<a href="ruta 1" class = "estiloAncla" id="link4"> historia 4</a>
</p>
<p class ="historia">……………..</p>
</body>

</html>
"""

#--------RECUPERO CONTENIDO------------
soup = BeautifulSoup(documento_html, "html.parser")
print(soup.prettify(), end="\n--------0---------\n")
#----------ACCEDO AL DOM---------------
print(soup.title, end="\n--------1---------\n")
print(soup.head, end="\n---------2--------\n")
print(soup.body, end="\n---------3--------\n")
print(soup.body.b, end="\n-------4----------\n")
print(soup.a, end="\n---------5--------\n")
#----USO FUNCIONES ESPECÍFICAS---------
soup.find_all('a')
#-----------CREO ARRAY-----------------
array = soup.find_all('a')
print(array[0], end="\n--------6---------\n")


#--------USO DE FUNCIONES--------------
#--ASIGNAR ETIQUETAS A VARIABLES-------
head_tag = soup.head
print(head_tag, end="\n--------7---------\n")
print(head_tag.contents, end="\n--------8---------\n")
body_tag = soup.body
for i in body_tag.children: print(i)
print('##########################################')
for i in body_tag.descendants: print(i)
#------Parent and .String--------------
print(head_tag.title.string, end="\n--------9---------\n")
print(head_tag.string, end="\n--------10---------\n")
print(head_tag.title.parent, end="\n--------11---------\n")
print(head_tag.parent, end="\n--------12---------\n")
#-----Búsqueda específica--------------
print(soup.find_all('p'), end="\n--------13---------\n")
print(soup.find_all(id='link2'), end="\n--------14---------\n")
print(soup.find_all("a", id='link2'), end="\n--------15---------\n")
#-Espreciones regulars (modulo re)-----
import re
for tag in soup.find_all(re.compile("^b")): print(tag.name)
for tag in soup.find_all(re.compile("t")): print(tag.name)
