import numpy as np


def es_subcadena(cadena, subcadena):
    """ Dada una subcadena y una cadena, devuelve True si la subcadena es es en efecto subcadena de cadena. Si no, False. """
    """
    Funciona comparando los bits de la subcadena con los de la cadena.
    Para cada bit, busca en la cadena la posición más cercana a 0 con ese bit.
    Cuando lo encuentre, guarda esa posición nueva y busca el siguiente bit desde la posición nueva
    hasta el final, más cercano al comienzo. Y así con todos los bits. Si hace un index out of range,
    es que no se ha encontrado un bit de la subcadena en lo que quedaba de la cadena, por tanto, no es subcadena. """

    posicion_en_cadena = 0
    for bit in subcadena:
        try:
            while(bit != cadena[posicion_en_cadena]):
                posicion_en_cadena += 1
            posicion_en_cadena += 1
        except:
            return False
    return True


def imprime_matriz(matriz):
    """ Tira de numpy pa dibujar la matriz en la terminal. """
    print(np.matrix(matriz))


def crear_matriz(cadena_a, cadena_b):
    """ Dadas dos cadenas, te inicializa la matriz
    de programación dinámica con todo cerapios y la
    primera fila y columna completada. Se podría hacer
    directamente en la otra función, pero te puedes volver loco
    con tanto if/elif/else, así que hemos decidido separarlo. """

    # Inicio matriz a ceros:
    matriz = [[0 for zero in range(len(cadena_b))]
              for x in range(len(cadena_a))]

    # Para cada posición matriz[x][0] o matriz[0][x],
    # asigno su valor de subcadena máximo, que viene siendo
    # que el bit 0 de una cadena esté contenido en la otra al menos 1 vez.
    for fila in range(len(cadena_a)):
        for columna in range(len(cadena_b)):
            if (fila == 0):
                if(cadena_a[0] in cadena_b[0:(columna+1)]):
                    matriz[fila][columna] = 1
                else:
                    matriz[fila][columna] = 0
            elif (columna == 0):
                if(cadena_b[0] in cadena_a[0:(fila+1)]):
                    matriz[fila][columna] = 1
                else:
                    matriz[fila][columna] = 0
    return matriz


def get_max_len(cadena_a, cadena_b):
    """Esta es la función principal."""

    # creo la matriz de 0s con fila 0 y columna 0 inicializada.
    matriz = crear_matriz(cadena_a, cadena_b)

    # para cada posición
    for fila in range(len(cadena_a)):
        for columna in range(len(cadena_b)):
            # descarto las filas ya hechas
            if(fila == 0 or columna == 0):
                continue
            # La magia es esta:
            # Si en anteriores iteraciones no he podido hacer una subcadena de la longitud de
            # la cadena que estudio, es porque me ha faltado el último bit.
            # Por tanto, si el último bit resulta ser igual que el bit con el que cuento en la
            # siguiente iteración, podré añadirlo y por tanto aumentar en 1 la longitud de la
            # subcadena máxima.
            elif(matriz[fila][columna-1] != (fila+1) and cadena_b[columna] == cadena_a[fila]):
                matriz[fila][columna] = matriz[fila][columna-1] + 1

            # Si no, el tamaño máximo será el tamaño máximo anterior.
            elif(matriz[fila][columna] < matriz[fila][columna-1]):
                matriz[fila][columna] = matriz[fila][columna-1]
    # Imprimo la matriz pa que se vea en terminal.
    imprime_matriz(matriz)

    # Y devuelvo la longitud máxima para las longitudes de las cadenas dadas.
    return matriz[len(cadena_a)-1][len(cadena_b)-1]


def binario(numero):
    """ Dado un nº devuelve su representación en binario"""
    return str(bin(numero))[2:]


def es_doble_subcadena(subcadena, a, b):
    """ Dadas dos cadenas a y b, una cadena es subcadena de ambas
    si es subcadena de a y subcadena de b. """
    return es_subcadena(a, subcadena) and es_subcadena(b, subcadena)


def get_ejemplo(cadena_a, cadena_b, max_len):
    """ una vez calculada la longitud máxima de cadena para
    unas cadenas dadas, genero todas las posibles cadenas con
    esa longitud, y las pruebo una por una para ver cuales
    son subcadenas de las cadenas a y b. """

    posibles_combinaciones = []
    for i in range(2**max_len):
        posibles_combinaciones.append(binario(i))
    posibles2 = []

    for posible in posibles_combinaciones:
        if(len(posible) != max_len):
            posible = str("0"*(max_len-len(posible))) + str(posible)
        posibles2.append(posible)
    resultados = []
    for posible in posibles2:
        if(es_doble_subcadena(posible, A, B)):
            resultados.append(posible)
    return resultados

# Programa principal


A = "01101010"
B = "101001001"


print(es_doble_subcadena("010101", A, B))

resultados = get_ejemplo(A, B, get_max_len(A, B))

print(resultados)
