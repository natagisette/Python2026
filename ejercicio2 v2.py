# hacer una funcion que tome como argumento un str y retorne el caracter que mas veces aparece
# y la cantidad de veces
# "hola!!!"   --> !, 3


def max_caracter(frase: str) -> tuple:
    caracter_max = ""
    cantidad_max = 0

    for caracter in frase:
        cantidad = frase.count(caracter)

        if cantidad > cantidad_max:
            cantidad_max = cantidad
            caracter_max = caracter

    return caracter_max, cantidad_max


print(max_caracter("yqwertynysymy"))
