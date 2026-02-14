##1. Return the second element of the given list. If the list has no second element, return None.
lista = []

def datos(lista):
    cant = int(input("ingrese la cantidad de datos: "))
    for i in range(cant):
        lista.append(input("ingrese un dato"))
        
def segDato(lista):
    try:
        if len(lista)<1:
            return None
        else: print(lista[1])
    except IndexError:
        print(" ")

datos(lista)
segDato(lista)
    