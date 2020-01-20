""" Ejercicios sesión 1 """


def es_primo(numero):
    """ Dado un numero, devuelve true si es primo """

    # Comparo el numero con cada uno de sus anteriores excepto el 1 y él mismo.
    for i in range(2, numero-1):
        # Si el resto es 0, no es primo.
        if (numero % i == 0):
            return False
    return True


def es_perfecto(numero):
    """ Dado un número, devuelve true si es perfecto, es decir,
    la suma de sus divisores propios positivos es el propio número """

    # Suma de divisores
    suma = 0

    for i in range(1, numero):
        # Para cada divisor, lo añado a la suma
        if (numero % (i) == 0):
            suma += (i)

    # Si el nº es igual a la suma de sus divisores, devuelvo True:
    if numero == suma:
        return True
    else:
        return False


def primos_y_perfectos(numero):
    """ Devuelve una lista de los numeros primos y perfectos
    que hay entre 1 y el numero dado"""
    # Lista de nºs entre 1 y el numero dado:
    numeros = [i for i in range(1, numero)]

    # Listas donde almacenaré los numeros que haya:
    primos = []
    perfectos = []

    for numero in numeros:
        # Primos:
        if(es_primo(numero)):
            primos.append(numero)
    # Perfectos:
        if(es_perfecto(numero)):
            perfectos.append(numero)

    return primos, perfectos


def sumatorio(numero):
    """ Devuelve recursivamente el sumatorio de 1 hasta el numero dado """

    # Caso base
    if (numero == 1):
        return numero

    # Caso general
    else:
        return sumatorio(numero-1) + numero


def Calculo(x, y, z):
    valor = 0

    for i in range(x, y):
        valor += i
        if ((valor//(x+y)) <= 1):
            return z
        else:
            print("he entrado al else")
            t = x+((y-x)//2)
            for i in range(x, y):
                for j in range(3*x, 3*y):
                    valor += min(i, j)
            valor += 4*Calculo(t, y, valor)
            return valor


for i in range(200):
    print(Calculo(7*i, 2*i, 1*i))
