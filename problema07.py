import libreria
import os

#hallar el tamaño del circulo
pi=float(os.sys.argv[1])
r=int(os.sys.argv[2])

tamano=libreria.tamano_circulo(pi,r)
print("el tamaño del circulo es:", tamano)
