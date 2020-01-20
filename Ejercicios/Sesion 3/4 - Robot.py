def ordenar_corchos(corchos, botellas, indice_pivote):
    """ Dados un array de corchos y botellas (numéricos),
    ordena los corchos de menor a mayor usando como pivotes las botellas.
    Para cada pivote se hace una llamada al propio método.
    """

    # Si ya se ha pivotado sobre todos los elementos de botellas,
    # se devuelven los corchos ordenados:
    if(indice_pivote >= len(botellas)):
        return corchos
    # Si no, se realiza el algoritmo:
    else:
        # Pivote de botellas
        pivote = botellas[indice_pivote]

        # Pivote en corcho contiene el índice del pivote en corchos
        indice_pivote_en_corchos = corchos.index(pivote)

        # Este índice contiene sobre qué elemento estamos pivotando en corchos:
        indice_recorrido = 0

        # Recorro todos los corchos:
        while(indice_recorrido < len(corchos)):

            # Si el elemento es mayor y estoy a la izquierda:
            if(corchos[indice_recorrido] > pivote and indice_recorrido < indice_pivote_en_corchos):
                valor = corchos[indice_recorrido]
                # Saco la parte de la izquierda
                seccion_izquierda = corchos[0:indice_pivote_en_corchos+1]
                # Elimino el elemento mayor a la izquierda del pivote
                seccion_izquierda.remove(valor)
                # Saco la parte derecha
                seccion_derecha = corchos[indice_pivote_en_corchos+1:]
                # Coloco el elemento mayor a la derecha del pivote
                corchos = seccion_izquierda + [valor] + seccion_derecha
                # Actualizo el indice del pivote en caso de que haya cambiado de sitio:
                indice_pivote_en_corchos = corchos.index(pivote)
            # Si el elemento es menor y estoy a la derecha:
            elif(corchos[indice_recorrido] < pivote and indice_recorrido >= indice_pivote_en_corchos):
                # Valor a reordenar:
                valor = corchos[indice_recorrido]
                # Saco la parte de la izquierda
                seccion_izquierda = corchos[0:indice_pivote_en_corchos]
                # Saco la parte derecha
                seccion_derecha = corchos[indice_pivote_en_corchos:]
                # Elimino el elemento menor a la derecha del pivote
                seccion_derecha.remove(valor)
                # Coloco el elemento mayor a la izquierda del pivote
                corchos = seccion_izquierda + [valor] + seccion_derecha
                # Actualizo el indice del pivote en caso de que haya cambiado de sitio:
                indice_pivote_en_corchos = corchos.index(pivote)
            # Si el elemento está correctamente ordenado:
            else:
                # Se avanza al siguiente elemento:
                indice_recorrido += 1
                indice_pivote_en_corchos = corchos.index(pivote)
        return ordenar_corchos(corchos, botellas, indice_pivote+1)


botellas = [1, 4, 6, 8, 3, 7]
corchos = [6, 8, 4, 1, 7, 3]
botellas2 = [38, 61, 65, 44, 88, 14, 76, 34, 17, 3, 18, 91, 77, 93, 16, 4, 59, 22, 57, 81, 13, 56, 48, 52, 39, 75, 25, 86, 74, 45, 58, 41, 95, 83, 66, 67, 54, 43, 11, 31, 99, 19, 55, 90, 92, 36, 84, 68,
             94, 89, 72, 7, 1, 15, 37, 62, 70, 60, 40, 0, 69, 5, 96, 24, 98, 73, 6, 27, 82, 33, 12, 35, 80, 21, 47, 32, 78, 49, 46, 10, 26, 71, 64, 28, 97, 51, 63, 53, 20, 79, 9, 29, 2, 50, 87, 8, 42, 30, 85, 23]
corchos2 = [36, 9, 26, 59, 8, 39, 31, 70, 88, 5, 16, 30, 34, 62, 3, 38, 67, 21, 77, 58, 0, 18, 56, 42, 52, 12, 7, 29, 20, 2, 43, 89, 84, 85, 99, 78, 87, 41, 37, 48, 98, 25, 33, 54, 92, 35, 82, 55, 49,
            24, 13, 94, 91, 57, 95, 97, 71, 40, 50, 53, 66, 76, 27, 69, 81, 68, 86, 96, 15, 51, 28, 14, 17, 11, 83, 79, 19, 73, 46, 44, 63, 74, 61, 60, 23, 22, 1, 80, 32, 72, 47, 64, 6, 93, 45, 90, 65, 4, 75, 10]


# Programa principal
print("Corchos: ", ordenar_corchos(corchos2, botellas2, 0))
print("Botellas: ", ordenar_corchos(botellas2, corchos2, 0))
