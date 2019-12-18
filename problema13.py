import libreria
import os

#hallar la suma de las areas totales del cilindro cuando su altura esta comprendido de 1 a 13
pi=float(os.sys.argv[1])
r=int(os.sys.argv[2])

suma_area_total=libreria.suma_area_total_cilindro(pi,r)
print("el area total del cilindro es:", suma_area_total)
