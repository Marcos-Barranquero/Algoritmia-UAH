import random


def masdeuncuarto(vector, veces, iteracion):
    posicion_aleatoria = random.randint(0, len(vector)-1)
    elemento_al_azar = vector[posicion_aleatoria]

    total = 0
    for i in range(1, len(vector)):
        if(vector[i] == elemento_al_azar):
            total += 1
    if(total > len(vector)/4) is True:
        return True
    elif(iteracion < veces):
        return masdeuncuarto(vector, veces, iteracion+1)
    else:
        return False


vector = [1, 1, 1, 1, 1, 4, 4, 4, 4, 2, 2, 2, 3, 3, 3, 3]
random.shuffle(vector)

print(masdeuncuarto(vector, 5, 0))
