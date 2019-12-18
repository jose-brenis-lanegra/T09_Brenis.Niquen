import libreria
import os

#hallar el area de un triangulo, de base mayor a 136 y de altura menor a 359
b=int(os.sys.argv[1])
a=int(os.sys.argv[2])

area=libreria.area_triangulo(b,a)
print("el area del triangulo es:", area)
