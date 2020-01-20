# Contador del numero de soluciones/formas distintas de reducir la cadena hasta un único carácter
contador = 0

def modificarCadena(cadena, long_cadena):
    # Si la longitud de la cadena es 1, hemos encontrado una solución, la sacamos por pantalla junto con su número de contador
    if long_cadena == 1:
        global contador
        print("Cadena resultante","(", contador,"): ", cadena)
        contador+=1
    
    # Bucle que examina todos los elementos de la cadena
    for i in range(long_cadena-1):
        # Se busca en el diccionario definido a ver que indice dentro de la tabla corresponde a cada letra de la cadena en sus respectivas posiciones.
        indice1 = indice_tabla.get(cadena[i])
        indice2 = indice_tabla.get(cadena[i+1])

        # Si las letras se encuentran en el diccionario, se puede intercambiar y se concatenan las letras a reemplazar con
        # el resto de la cadena a partir de las 2 letras sustituidas.
        if (indice1 is not None) and (indice2 is not None):
            nueva_cadena = "".join([cadena[:i], tabla[indice1][indice2], cadena[i+2:]])
            modificarCadena(nueva_cadena, len(nueva_cadena))
        # Si alguna de las letras no se encuenta en el diccionario, no se puede reemplazar y por lo tanto no se podrá encontrar una solución de 1 solo carácter.
        else:
            print("No se podrá reducir a 1 solo carácter.")
            break


# Se inicializa la tabla, se ha cogido la tabla que viene en el enunciado.
def inicializarTabla():
    tabla[0][0] = "b"
    tabla[0][1] = "b"
    tabla[0][2] = "a"
    tabla[0][3] = "d"

    tabla[1][0] = "c"
    tabla[1][1] = "a"
    tabla[1][2] = "d"
    tabla[1][3] = "a"

    tabla[2][0] = "b"
    tabla[2][1] = "a"
    tabla[2][2] = "c"
    tabla[2][3] = "c"

    tabla[3][0] = "d"
    tabla[3][1] = "c"
    tabla[3][2] = "d"
    tabla[3][3] = "b"

# Tabla de referencias de a que posicion corresponde cada letra en la tabla generada
indice_tabla = {
    "a":0,
    "b":1,
    "c":2,
    "d":3
}

# Programa principal
tabla = [["" for _ in range (4)] for _ in range(4)]
inicializarTabla()

texto = "acabada"
n = len(texto)
modificarCadena(texto, n)