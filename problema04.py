import libreria
import os

#hallar el perimetro del romboide
b=int(os.sys.argv[1])
a=int(os.sys.argv[2])

perimetro=libreria.perimetro_romboide(b,a)
print("el perimetro del romboide es:", perimetro)
