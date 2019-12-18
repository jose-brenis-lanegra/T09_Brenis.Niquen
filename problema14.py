import libreria
import os

#hallar el area lateral del cono
pi=float(os.sys.argv[1])
r=int(os.sys.argv[2])
a=int(os.sys.argv[3])

area_lateral=libreria.area_lateral_cono(pi,r,a)
print("el area lateral del como es:", area_lateral)
