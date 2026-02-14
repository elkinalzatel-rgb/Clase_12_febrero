from random import randint
equipos = [[]]
nomEquipos = ["Juan", "Marcos", "Luis", "Miguel"]
def integrantes(eq):
    for i in range(cantT-1):
        for j in range(cantP-1):
            eq[i][j] = nomEquipos[randint(0,3)]
def selec(eq):
    return eq[cantT-1][1] 

cantT = int(input("ingrese la cantidad de equipos"))
cantP = int(input("ingrese la cantidad de jugadores por equipo"))
integrantes(equipos)
selec(equipos)
