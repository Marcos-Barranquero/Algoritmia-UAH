pesos = [2, 3, 4, 5, 7, 9, 12, 15, 17]
valores = [3, 5, 6, 10, 13, 15, 20, 24, 27]

print(len(pesos) == len(valores))

numero_objetos = len(pesos)
peso_maximo = 8


def mochila_backtracking(evaluar_a_partir_de, peso_maximo):
    solucion_optima = 0
    for este_objeto in range(evaluar_a_partir_de, numero_objetos):
        if (pesos[este_objeto] <= peso_maximo):
            solucion_optima = max(solucion_optima, valores[este_objeto] + mochila_backtracking(
                este_objeto, peso_maximo - pesos[este_objeto]))
    return solucion_optima


res = mochila_backtracking(0, 40)
print(res)
