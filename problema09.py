import libreria
import os

#hallar el tipo del cuadrilatero encontrado
l1=int(os.sys.argv[1])
l2=int(os.sys.argv[2])
l3=int(os.sys.argv[3])
l4=int(os.sys.argv[4])

tipo=libreria.tipo_cuadrilatero(l1,l2,l3,l4)
print("el tipo del cuadrilatero es:", tipo)
