
def ocho_reinas(num_reinas, columnas_usadas, diagonal_45, diagonal_135, solucion):
    # Si hemos colocado las 8 ya printeamos
    if(num_reinas >= 8):
        print(solucion)
    # si no pues seguimos que se le va a hacer
    else:
        for i in range(8):
            # Si no hemos usado esa columna ya ni tiene conflictos con ninguna de las diagonales
            if((i not in columnas_usadas) and (i+num_reinas not in diagonal_45) and (i-num_reinas not in diag135)):
                # Sorpresa, es solucion
                solucion[num_reinas] = i
                # Usamos listas temporales para evitar los tremendos punteros
                temp_usadas = list(columnas_usadas)
                temp_usadas.append(i)
                temp_diag_45 = list(columnas_usadas)
                temp_diag_45.append(i+num_reinas)
                temp_diag_135 = list(columnas_usadas)
                temp_diag_135.append(num_reinas)
                # Se llama a la funcion de nuevo con la solucion parcial
                ocho_reinas(num_reinas+1, temp_usadas, temp_diag_45, temp_diag_135, solucion)


# Caca pruebamientacion
col = []
diag45 = []
diag135 = []
sol = [0 for i in range(8)]
ocho_reinas(0,col, diag45, diag135, sol)