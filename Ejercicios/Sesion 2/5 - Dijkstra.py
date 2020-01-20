import math


def dijkstra(nodos, matriz_costes):
    # Lista de nodos en el orden visitado hasta llegar a la solución.
    camino = []
    candidatos = list(nodos)  # Lista de nodos aún no tomados en el camino.

    primero = nodos[0]

    camino.append(primero)  # Añado primer nodo
    candidatos.remove(primero)  # Quito el primero puesto que ya lo he tomado.
    # Elimino el primer nodo de la lista de nodos restantes.
    nodos.remove(primero)

    # Añado en el array distancias las distancias del primer nodo al resto.
    distancias = []
    for i in range(1, len(matriz_costes[0])):
        distancias.append(matriz_costes[0][i])

    # Mientras aún haya candidatos:
    while candidatos:

        # Buscaré el nodo con el camino mínimo en el array de distancias:
        coste_camino_minimo = math.inf
        nodo_camino_minimo = None
        for coste_camino in distancias:
            nodo = distancias.index(coste_camino) + 1

            # Si encuentro un camino más barato a un nodo sin visitar que el
            # anterior, lo tomo:
            if coste_camino < coste_camino_minimo and nodo in candidatos:
                nodo_camino_minimo = nodo
                coste_camino_minimo = coste_camino

        # Una vez tomado el nodo cuyo camino es más barato, lo elimino de candidatos.
        candidatos.remove(nodo_camino_minimo)

        # ... y lo añado al camino seguido:
        camino.append(nodo_camino_minimo)

        # Y actualizo la matriz de costes:
        coste_distancias_nodo_minimo = []
        for i in range(1, len(matriz_costes[nodo_camino_minimo])):
            coste_distancias_nodo_minimo.append(
                matriz_costes[nodo_camino_minimo][i])

        # Después, actualizo distancias en caso de hayar un camino más barato a un nodo:
        for i in range(len(distancias)):
            distancias[i] = min(
                distancias[i], coste_camino_minimo + coste_distancias_nodo_minimo[i])

    # Finalmente, calculo el coste:
    coste_camino = 0
    for i in range(len(camino)-1):
        # Sumo el coste de ir del nodo camino[i] al nodo camino[i+1]
        coste_camino += matriz_costes[camino[i]][camino[i+1]]
    return coste_camino, camino


if __name__ == '__main__':

    #     20
    # |0|--->|1|
    #  |     ^|
    # 3|  1/  |2
    #  v /    v
    # |2|--->|3|
    #     4

    nodos = [0, 1, 2, 3]
    matriz_costes = [
        [0, 20, 3, math.inf],
        [math.inf, 0, math.inf, 2],
        [math.inf, 1, 0, 4],
        [math.inf, math.inf, math.inf, 0]
    ]

    coste, camino_minimo = dijkstra(nodos, matriz_costes)
    print("Coste: ", coste, "Camino: ", camino_minimo)
