def shrek(escaleras):
    """ Para que la suma acumulada sea la menor, deben de soldarse
    escaleras de menor a mayor coste.
    """

    suma = 0
    for escalera in escaleras:
        suma = suma*2 + escalera
    print(suma)

    escaleras.sort()
    # Una vez ordenadas, se acumula el coste:
    suma = 0

    print(escaleras)
    for escalera in escaleras:
        suma = suma*2 + escalera
    return suma


escaleras = [1, 6, 4, 1, 5, 8]
tiempo = shrek(escaleras)
print(tiempo)
