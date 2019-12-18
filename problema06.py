import libreria
import os

#hallar la suma de las area de un hexagono cuando el apotema esta comprendido de 1 a 16
bh=int(os.sys.argv[1])

suma_area=libreria.suma_area_hexagono(bh)
print("la suma de las area del hexagono es:", suma_area)
