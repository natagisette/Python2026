# dada una frase y un diccionario con los pesos de las palabras
# calcular el porcentaje de positividad del texto
# Buscar las palabras que estan en la frase y calcular el promedio segun el peso del diccionario
# si la palabra no esta en el diccionario el peso es cero


diccionario_pesos = {
    "estoy": 5,
    "feliz": 10
}


def positividad(frase: str) -> float:
    palabras = frase.split()
    suma = 0

    for palabra in palabras:
        if palabra in diccionario_pesos:
            suma += diccionario_pesos[palabra]
        else:
            suma += 0

    promedio = suma / len(palabras)
    return promedio


frase = "estoy en un mundo feliz"

promedio = positividad(frase)

print("promedio", promedio)
