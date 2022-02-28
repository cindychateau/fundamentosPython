#Funciones
def sumatoria(a, b):
    suma = a+b
    print(suma)

def sumatoriaReturn(a, b):
    suma = a+b
    return suma

def helloWorld(nombre="John", apellido="Doe"):
    print(f"Hello world {nombre} {apellido}")

sumatoria(1, 2)

sum = sumatoriaReturn(3, 4)
print(sum)

#helloWorld("Cynthia", "Castillo")
helloWorld(apellido="Castillo", nombre="Cynthia")
