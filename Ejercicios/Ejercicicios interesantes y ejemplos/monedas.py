

# FUNCTION

def imprimir_matriz(matriz):
    a = ""
    for k in range(3):
        for j in range(3):
            # print(m[k][j])
            a += str(matriz[k][j])+'\t'
        print(a)
        a = ""


def cambio_optimo(cambio_total):
    # Array de monedas que tenemos que combinar
    posibles_monedas = [1, 2, 5, 10, 20, 50, 100]
    # posibles_monedas = [1,4,6]
    # Cantidad de las posibles monedas disponibles
    n = len(posibles_monedas)

    # Se inicializa la matriz a 0
    k = [[0 for i in range(cambio_total+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(cambio_total+1):
            # Esta linea no vale para nada si quiera porque ya eran 0 al inicializarlo arriba asi que no se pero lo dejo para decorar feliz navidad
            # if(i == 0 or j == 0):
            #    k[i][j] = 0
            # Si estamos en la primera fila que vale para algo sucede la magia
            # if(i == 1):
            #    k[1][j] = 1 + k[1][j-posibles_monedas[0]]
            # Si estamos en una fila superior a la primera se empiezan a hacer comprobaciones
            # Si el numero de monedas a devolver es menor que la nueva moneda introducida, se copia lo de la fila anteior
            if(j < posibles_monedas[i-1]):
                k[i][j] = k[i-1][j]
            # Si se puede usar la nueva moneda introducida, se calcula el minimo entre la fila anterior y el resultado de usar esta nueva moneda
            else:
                k[i][j] = min(k[i-1][j], 1 + k[i][j-posibles_monedas[i-1]])
    imprimir_matriz(k)
    return k[n][cambio_total]


def cambio_superoptimo(cambio_total):
        # Array de monedas que tenemos que combinar
    posibles_monedas = [1, 2, 5, 10, 20, 50, 100]
    # posibles_monedas = [1,4,6]
    # Cantidad de las posibles monedas disponibles
    n = len(posibles_monedas)
    filas = n
    columnas = cambio_total

    # Se inicializa la matriz a 0
    k = [[0 for i in range(cambio_total)] for j in range(n)]

    for fila in range(filas):
        for columna in range(columnas):
            try:
                k[fila][columna] = min(
                    1 + k[fila][columna-1], k[fila-1][columna])
            except:
                k[fila][columna] = 1
    imprimir_matriz(k)
    return k[filas-1][columnas-1]


# DRIVER CODE


print(cambio_superoptimo(162))
