import libreria
import os

#hallar que tipo de raices tiene la ecuacion
a=int(os.sys.argv[1])
b=int(os.sys.argv[2])
c=int(os.sys.argv[3])

raiz=libreria.raices(a,b,c)
print("las raices de la ecuacion son:", raiz)
