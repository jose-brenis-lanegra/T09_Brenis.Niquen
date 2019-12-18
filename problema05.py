import libreria
import os

#hallar el area de un trapecio
bma=int(os.sys.argv[1])
bme=int(os.sys.argv[2])
a=int(os.sys.argv[3])

area=libreria.area_trapecio(bma,bme,a)
print("el area del trapecio es:", area)
