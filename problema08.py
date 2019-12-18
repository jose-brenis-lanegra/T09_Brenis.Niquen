import libreria
import os

#calcular el tipo de elipse
sma=int(os.sys.argv[1])
sme=int(os.sys.argv[2])

tipo=libreria.tipo_elipse(sma,sme)
print("el tipo de elipse es:", tipo)
