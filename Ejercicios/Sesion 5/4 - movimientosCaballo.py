
def caballo(tablero, posx, posy, num_movimientos):
    # Si el numero de movimientos es mayor o igual que el numero total de casillas, es que hemos visitado todas las casillas,
    # por lo que hemos encontrado una solución.
    if num_movimientos >= filas * columnas:
        print("Solución encontrada para los parámetros:")
        print("\tTamaño del tablero (Filas x Columnas): ",filas,"x",columnas)
        print("\tPosición inicial: ", pos_inicial)
        return True

    for fila in range(filas):
        for columna in range(columnas):
            # Si el movimiento es válido y la casilla no ha sido visitada aún
            if movimiento_valido(posx, posy, fila, columna) and tablero[fila][columna] == 0:

                # Marco la casilla como visitada
                tablero[fila][columna] = 1

                # Llamo recursivamente a las posibles soluciones derivadas de este paso
                exito = caballo(tablero, fila, columna, num_movimientos+1)

                # Marco la casilla como no visitada
                tablero[fila][columna] = 0

                if exito:
                    return True

def movimiento_valido(n_fila_ini, n_columna_ini, n_fila_fin, n_columna_fin):
    """ Devuelve true si el movimiento es correcto. Si no, False. """
    return (abs(n_fila_fin - n_fila_ini) == 1 and abs(n_columna_fin - n_columna_ini) == 2) or (abs(n_fila_fin - n_fila_ini) == 2 and abs(n_columna_fin - n_columna_ini) == 1)

# Programa principal
filas = 6
columnas = 6
pos_inicial = [0, 0] # fila, columna
tablero = [[0 for columna in range(columnas)] for fila in range(filas)]
# Se marca la posicion inicial como visitada
tablero[pos_inicial[0]][pos_inicial[1]] = 1
# Si la funcion ha terminado y no ha retornado nada, es que no hay solución
if caballo(tablero, pos_inicial[0], pos_inicial[1], 1) is None:
    print("No hay ninguna solución para los parámetros introducidos.")