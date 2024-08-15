def combinar_cadenas(lista):
    cadena = ""
    for i, palabra in enumerate(lista):
        if i > 0:
            cadena += " "
        cadena += palabra
    return cadena

lista_cadenas = ["Hola", "mundo", "como", "estan", "hoy"]
print("Cadena combinada:", combinar_cadenas(lista_cadenas))
