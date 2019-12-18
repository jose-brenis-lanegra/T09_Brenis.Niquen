import libreria
import os

#hallar el volumen de una piramide
ar=int(os.sys.argv[1])
al=int(os.sys.argv[2])

volumen=libreria.volumen_piramide(ar,al)
print("el volumen de la piramide es:", volumen)
