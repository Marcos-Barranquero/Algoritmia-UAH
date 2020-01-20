"""Se tienen n números naturales, siendo n una cantidad par, que tienen que juntarse
formando parejas de dos números cada una. A continuación, de cada pareja se obtiene la
suma de sus dos componentes, y de todos estos resultados se toma el máximo.
Diseñar un algoritmo voraz que cree las parejas de manera que el valor máximo de las
sumas de los números de cada pareja sea lo más pequeño posible, demostrando que la
función de selección de candidatos usada proporciona una solución óptima.
Ejemplo: suponiendo que los datos se encuentran en el vector siguiente: 5 8 1 4 7 9
"""


def mejores_parejas(vector):
    # Paso 1: ordenar el vector
    vector.sort()

    print(vector)

    # Paso 2: tomar parejas de extremos opuestos
    parejas = []

    for i in range(len(vector)//2):
        # Tomo el primero
        p1 = vector[0]
        # y lo elimino
        vector.remove(p1)
        # Saco el segundo
        p2 = vector.pop()
        # Creo la pareja y la inserto en parejas:
        parejas.append((p1,p2))
    print(parejas)

    # Paso 3: busco la pareja máxima:
    maximo = 0
    pareja_maxima = (0, 0)
    for pareja in parejas:
        if pareja[0] + pareja[1] > maximo:
            pareja_maxima = pareja
    return pareja_maxima

# Programa principal


mejor = mejores_parejas([5, 8, 1, 4, 7, 9])
print(mejor)
