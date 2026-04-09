# Python2026
Ejercicios 2 ano

# Hacer una funcion que tome como argumento una lista de numeros y retorne el menor valor de la lista.


def menor(numeros: list) -> int:
    menor_numero = numeros[0]

    for numero in numeros:
        if numero < menor_numero:
            menor_numero = numero

    return menor_numero


lista = [5, 7, 8, 9, 4]

resultado = menor(lista)

print("menor:", resultado)
