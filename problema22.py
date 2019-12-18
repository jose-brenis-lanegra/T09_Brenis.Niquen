import libreria
import os

#demostrar si se puede acceder a una caja fuerte
cad1=os.sys.argv[1]
cad2=os.sys.argv[2]

caja=libreria.comparacion_len(cad1,cad2)
print("¿se puede acceder a la caja fuerte?:", caja)
