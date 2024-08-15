def factorial(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos") 
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado

numeros_a_probar = [0, 1, 5, 7]
for numero in numeros_a_probar:
    print(f"Factorial de {numero} es: {factorial(numero)}")
