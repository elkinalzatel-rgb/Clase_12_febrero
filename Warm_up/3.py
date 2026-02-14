listaR = ["c1", "c2", "c3", "c4"]
def swap(lista):
    print(lista)
    a = lista[0]
    b = lista[len(lista)-1]
    lista[0] = b
    lista[len(lista)-1] = a
    print(lista)
swap(listaR)