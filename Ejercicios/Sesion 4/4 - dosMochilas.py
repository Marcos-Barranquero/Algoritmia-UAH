def optimizar_valor_mochila(capacidad, array_pesos, array_valores):
    # Obtengo el numero de elementos
    numero_objetos = len(array_pesos)

    # Genero la matriz y la relleno de ceros
    matriz = [[0 for zero in range(capacidad+1)]
              for x in range(numero_objetos+1)]

    # Relleno la matriz con los valores de los arrays
    for fila in range(numero_objetos+1):
        for columna in range(capacidad+1):
            # Si no tienes objetos ni capacidad:
            if fila == 0 or columna == 0:
                matriz[fila][columna] = 0
            elif array_pesos[fila-1] <= columna:
                # Si el nuevo objeto estudiado tiene un peso inferior a
                # la capacidad máxima de la mochila (columna),
                # compruebo si me sale mejor quedarme como estaba (es decir,
                # estudiar los objetos que tomaría si no tuviese ese nuevo objeto)
                # o, por el contrario, añadir ese nuevo objeto y estudiar qué podría
                # meter en el espacio restante.
                matriz[fila][columna] = max(array_valores[fila-1]
                                            + matriz[fila-1][columna-array_pesos[fila-1]],
                                              matriz[fila-1][columna])
            else:
                # Si no puedo meter el nuevo objeto porque su peso es superior a mi
                # capacidad en ese momento, me quedo como estaba, es decir,
                # tomando los objetos que tomé en la iteración anterior. (Con capacidad-1)
                matriz[fila][columna] = matriz[fila-1][columna]
    
    
    # Lista de valores que se han utilizado, usando el peso de los elementos utilizados.
    lista_usados = []
    # Se guardan en variables locales algunos valores para
    #  poder modificarlos sin alterar el resultado
    resultado = matriz[numero_objetos][capacidad]
    capacidad_temp = capacidad
    
    # Mirando desde el final de la tabla generada
    for i in range(numero_objetos, 0, -1):
        # Si ya hemos llegado al principio de la tabla, es decir, si ya hemos examinado 
        # todos los posibles valores, salimos del bucle
        if resultado <= 0: 
            break
        # Se evalua de donde vienen los valores almacenados en la tabla
        # Si es igual al valor que se encuentra en la fila anterior, el bucle continua examinando
        if resultado == matriz[i - 1][capacidad_temp]: 
            continue
        # Si no es igual, esto quiere decir que el elemento de la fila que estamos 
        # evaluando ha sido utilizado para obtener el valor óptimo,
        # por lo que se añade a la lista de elementos utilizados.
        else: 
            lista_usados.append(array_pesos[i-1])
            # Una vez añadido a la lista, se resta el valor de ese elemento del resultado
            resultado = resultado - array_valores[i - 1] 
            # Y se resta tambien el peso para recolocarnos en la tabla en la 
            # posicion correcta y poder seguir evaluando
            capacidad_temp = capacidad_temp - array_pesos[i - 1]

    return matriz[numero_objetos][capacidad], lista_usados


def mochilero_dos_mochilas(limite_mochila1, limite_mochila2, array_pesos, array_valores):
    # Fuerzo a que mochila 1 sea la de mayor capacidad.
    temp = limite_mochila1
    limite_mochila1 = max(lim_mochila1, limite_mochila2)
    limite_mochila2 = max(temp, limite_mochila2)

    # Calculo el valor óptimo que puedo almacenar con la mochila 1:
    optimo_mochila1, lista_usados_uno = optimizar_valor_mochila(
        limite_mochila1, array_pesos, array_valores)

    # Calculo los arrays de los objetos que quedan:
    que_elementos_quedan(lista_usados_uno, array_pesos, array_valores)

    # Calculo el valor óptimo que puedo almacenar con la mochila 2:
    optimo_mochila2, lista_usados_dos = optimizar_valor_mochila(
        limite_mochila2, array_pesos, array_valores)

    return optimo_mochila1, optimo_mochila2

# La funcion se encarga de eliminar de los arrays de pesos 
# y valores aquellos elementos que ya hallan sido utilizados
# a partir de la lista devuelta por la primera llamada a la funcion de optimización.
def que_elementos_quedan(lista_usados, array_pesos, array_valores):
    n = len(lista_usados)
    for i in range(n):
        indice = array_pesos.index(lista_usados[i])
        array_pesos.pop(indice)
        array_valores.pop(indice)


# Programa principal
array_valores = [1, 6, 18, 22, 28]
array_pesos = [1, 2, 5, 6, 7]
lim_mochila1 = 11
lim_mochila2 = 8


om1, om2 = mochilero_dos_mochilas(
    lim_mochila1, lim_mochila2, array_pesos, array_valores)

print("Optimo con la mochila 1: ", om1)
print("Optimo con la mochila 2 y los elementos restantes: ", om2)
