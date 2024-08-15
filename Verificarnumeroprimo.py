import math

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    limite = int(math.sqrt(n)) + 1
    for i in range(5, limite, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

numero = 29
print(f"¿El número {numero} es primo? {es_primo(numero)}")
