import os
from tkinter import *
from PIL import Image


def crear_thumbs(directorio, size=(100, 100), subdirectorio="thumbs"):

    directorioParaThumb = os.path.join(directorio, subdirectorio)
    if not os.path.exists(directorioParaThumb):
        os.mkdir(directorioParaThumb)

    for imagen in os.listdir(directorio):
        thumbpath = os.path.join(directorioParaThumb, imagen)
        print("Creando", thumbpath)
        imgpath = os.path.join(directorio, imagen)
        try:
            imgobj = Image.open(imgpath)
            imgobj.thumbnail(size, Image.ANTIALIAS)
            imgobj.save(thumbpath)
        except:
            print("Skipping: ", imgpath)


if __name__ == "__main__":
    directorioImagenes = "images"
    thumbs = crear_thumbs(directorioImagenes)