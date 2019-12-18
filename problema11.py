import libreria
import os

#hallar el volumen del prisma
la=int(os.sys.argv[1])
an=int(os.sys.argv[2])
al=int(os.sys.argv[3])

volumen=libreria.volumen_prisma(la,an,al)
print("el volumen del prisma es:", volumen)
