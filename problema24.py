import libreria
import os

#hallar la posicion de "V" en el mensaje
msg=os.sys.argv[1]

bus=libreria.busqueda(msg)
print("la V en el mensaje esta en la posicion:", bus)
