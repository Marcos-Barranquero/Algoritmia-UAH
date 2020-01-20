def funcion(x):
    # return (((x+10)**2))-20
    # return (((x+50)**2))-200
    return x**2


def valle_minimo_fun(principio, final):
    """ Dado el principio y el final del puente, y 
    una funcion auxiliar que define la curva, retorna
    la posición (X) donde se encuentra la profundidad (Y)
    más profunda (la mayor)"""

    # Calculo distancia del espacio a estudiar:
    distancia = final - principio

    # Si es menor que 3, devuelvo el punto de mayor profundidad
    if(distancia < 3):
        # Valor mínimo retornado por la función
        posicion_minimo = principio
        for i in range(principio, final+1):
            if(funcion(i) < funcion(posicion_minimo)):
                posicion_minimo = i
        return posicion_minimo

    # Si no, calculo el tamaño de un tercio:
    tercio = distancia//3

    # Calculo el último elemento del primer tercio:
    elemento1 = funcion(principio + tercio)

    # Calculo el primer elemento del último tercio
    elemento2 = funcion(principio + 2*tercio)

    # Si los dos primeros tercios son más profundos, descarto el tercero
    if(elemento1 <= elemento2):
        return valle_minimo_fun(principio, final-tercio)

    # Si los dos segundos tercios son más profundos, descarto el primero
    elif(elemento1 > elemento2):
        return valle_minimo_fun(principio+tercio, final)


print(valle_minimo_fun(-10, 100))
