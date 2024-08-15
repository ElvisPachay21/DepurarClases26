def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

lista_numeros = [1, 2, 3, 4, 5, 6]
print("Números pares:", filtrar_pares(lista_numeros))  

lista_numeros_negativos = [-5, -4, -3, -2, -1, 0]
print("Números pares:", filtrar_pares(lista_numeros_negativos)) 

lista_numeros_mixta = [0, 7, -14, 22, -9]
print("Números pares:", filtrar_pares(lista_numeros_mixta)) 