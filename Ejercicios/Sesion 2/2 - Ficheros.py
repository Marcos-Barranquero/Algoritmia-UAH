from random import randint


class fichero(object):
    """clase fichero que almacena la informacion sobre los ficheros que van a estar en la cinta"""
    longitud = 0
    llamadas = 0

    def __init__(self, x, y):
        self.longitud = x
        self.llamadas = y

    def __str__(self):
        cadena = "Long: ", self.longitud, "; Llamadas: ", self.llamadas, "L/ll: ", (
            self.longitud/self.llamadas)
        return str(cadena)

    __repr__ = __str__


def inicializar_cinta(n):
    """ Este metodo se encarga de inicializar el vector con n ficheros y valores aleatorios"""
    ficheros = []
    for _ in range(n):
        ficheros.append(fichero(randint(1, 200), randint(1, 50)))
    return ficheros


def ordenar_cinta(ficheros):
    """Este metodo se encarga de ordenar la cinta magnetica
    Para ello, dividir el valor de la longitud del fichero por el numero de llamadas que se le va a hacer
    Despues de hacer esta division, se ordenan usando el algoritmo de la burbuja
    De esta forma se consigue que los ficheros se almacenen en el orden mas eficiente"""
    long = len(ficheros)
    # Algoritmo de la burbuja:
    for i in range(long):
        for j in range(0, long-i-1):
            if ((ficheros[j].longitud / ficheros[j].llamadas)) > ((ficheros[j+1].longitud / ficheros[j+1].llamadas)):
                ficheros[j], ficheros[j+1] = ficheros[j+1], ficheros[j]
    print(ficheros)
    return ficheros

# Metodo de prueba


def test():
    ficheros = ordenar_cinta(inicializar_cinta(20))
    for obj in ficheros:
        print("Long: ", obj.longitud, "Llamadas: ",
              obj.llamadas, "LL: ", obj.longitud/obj.llamadas)


test()
