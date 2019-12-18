def area_triangulo(base,altura):
    res=(base*altura)/2
    while (base <= 136 or altura >= 359):
        base = float(input("ingrese la base:"))
        altura = float(input("ingrese la altura:"))
        res= (base * altura) / 2
    return res
#fin funcion

def area_cuadrado(lado):
    res=lado**2
    return res
#fin funcion

def area_rombo(diagonal_menor,diagonal_mayor):
    res=(diagonal_mayor*diagonal_menor)/2
    return res
#fin funcion

def perimetro_romboide(base,altura):
    res=2*base+2*altura
    while (base < 99 and altura >= 98):
        base = float(input("ingrese base:"))
        altura = float(input("ingrese altura:"))
        res = 2 * base + 2 * altura
    return res
#fin funcion

def area_trapecio(base_mayor,base_menor,altura):
    res=(altura*(base_mayor+base_menor))/2
    return res
#fin funcion

def suma_area_hexagono(base_h):
    area=0
    for apotema in range(4, 17):
        print(apotema)
        area = area + (6 * base_h * apotema) / 2
    return area
#fin funcion

def tamano_circulo(pi,radio):
    area=pi*(radio**2)
    if (area > 100):
        return "circulo grande"
    if (100 >= area > 50):
        return "circulo mediano"
    if (0< area <= 50):
        return "circulo pequeño"
#fin funcion

def tipo_elipse(semieje_mayor,semieje_menor):
    if (semieje_menor < semieje_mayor):
        return "elipse horizontal"
    if (semieje_mayor < semieje_menor):
        return "elipse vertical"
    if (semieje_menor == semieje_mayor):
        return "circulo"
#fin funcion

def tipo_cuadrilatero(lado_1,lado_2,lado_3,lado_4):
    if (lado_1 != lado_2 != lado_3 != lado_4):
        return "cuadrilatero comun"
    if (lado_1 == lado_3 or lado_2 == lado_4):
        return "rectangulo"
    if (lado_1 == lado_2 == lado_3 == lado_4):
        return "cuadrado"
#fin funcion

def volumen_cubo(arista):
    res=arista**3
    return res
#fin funcion

def volumen_prisma(largo,ancho,altura):
    res=largo*ancho*altura
    return res
#fin funcion

def demostrar_esfera(pi,radio):
    volumen=(4*pi*(radio**3))/3
    if (volumen < radio):
        return "incoherente"
    if (volumen == radio):
        return "extraño"
    if (volumen > radio):
        return "corrcecto"
#fin funcion

def suma_area_total_cilindro(pi,radio):
    altura=1
    while (altura < 14):
        print(altura)
        altura += 1
        area = 2 * pi * radio * (radio + altura)
    return area
#fin funcion

def area_lateral_cono(pi,radio,altura):
    res=pi*radio*((radio*2+altura*2)**(1/2))
    return res
#fin funcion

def volumen_piramide(arista,altura):
    res=(arista**2)*altura/3
    return res
#fin funcion

def volumen_teraedro(arista):
    res=((2**(1/2))*(arista**3))/12
    return res
#fin funcion

def volumen_octaedro(arista):
    res=((2**(1/2))*(arista**3))/3
    return res
#fin funcion

def volumen_dodecaedro(arista):
    res=((15+(7*(5**(1/2))))*(arista**3))/4
    return res
#fin funcion

def volumen_icosaedro(arista):
    res=(5*(3+(5**(1/2)))*(arista**3))/12
    return res
#fin funcion

def raices(a,b,c):
    discriminate=(b**2)-(4*a*c)
    if (discriminate < 0):
        return "raices complejas"
    else:
        return "raices reales"
#fin funcion

def palindromo(cadena):
    invertida=cadena[::-1]
    if (invertida==cadena):
        return True
    else:
        return False
#fin funcion

def comparacion_len(cadena1,cadena2):
    if (len(cadena1)==len(cadena2)):
        acceso="concedido"
        return acceso
    else:
        acceso="denegado"
        return acceso
#fin funcion

def cortar(cadena):
    new=cadena[:8]+cadena[12:]
    return new
#fin funcion

def busqueda(mensaje):
    res=mensaje.find("A")
    return res
#fin funcion

def longitud(palabra):
    rpta=len(palabra)
    return rpta
#fin funcion
