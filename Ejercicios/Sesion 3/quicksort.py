def ordenar_por_quicksort(vector):
    if(len(vector) == 2):
        return vector
    puntero_pivote = len(vector)//2
    puntero_izquierdo = 0
    puntero_derecho = len(vector)-1
    print("Indice pivote: ", puntero_pivote,
          "; vector[pivote] = ", vector[puntero_pivote])
    while(puntero_derecho != puntero_pivote and puntero_izquierdo != puntero_pivote):
        print(vector)
        while(vector[puntero_izquierdo] < vector[puntero_pivote] and puntero_izquierdo != puntero_pivote):
            print(vector[puntero_izquierdo], "<", vector[puntero_pivote])
            puntero_izquierdo += 1
        while(vector[puntero_derecho] > vector[puntero_pivote] and puntero_derecho != puntero_pivote):
            print(vector[puntero_derecho], ">", vector[puntero_pivote])
            puntero_derecho -= 1
        if(vector[puntero_izquierdo] > vector[puntero_pivote] and vector[puntero_derecho] < vector[puntero_pivote]):
            vector[puntero_izquierdo], vector[puntero_derecho] = vector[puntero_derecho], vector[puntero_izquierdo]

    lado_izquierdo = ordenar_por_quicksort(vector[0:puntero_pivote])
    pivote = vector[puntero_pivote]
    lado_derecho = ordenar_por_quicksort(vector[puntero_pivote:])


vect = [8, 3, 6, 4, 2, 5, 7, 1]
ordenar_por_quicksort(vect)
