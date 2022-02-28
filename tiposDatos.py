#Booleans
boolean = True #True o False

#Numerales
num = 10
fl = 10.34
nuevoFloat = float(90)
nuevoEntero = int(10.99)
print(nuevoEntero)
print(nuevoFloat)

import random
numAleatorio = random.randint(2,5) #Aleatorio entre 2 y 5
print(numAleatorio)

#Cadena
string = "ABDCEFG"
print("Este es un string:", string) #el coma en automático me va a agregar un espacio
print("Este es un segundo string "+string)
print("Este un numero", numAleatorio) #agrega espacio
#print("Este es num"+numAleatorio) ERROR
print("Este es un num" + str(numAleatorio))
print(f"Este es el alfabeto {string}") #Dentro de las llaves ponemos la variable
print("Este es el abecedario %s, y este es un num %d" % (string, num))

#Metodos para cadenas
cadena = "Buenas tardes a Todos tardes"
cadena2 = "Buenas tardes a Todos"
print(cadena.title()) #Primera letra de cada palabra sea mayúscula
print(cadena.upper()) #TODAS mayúsculas
print(cadena.lower()) #TODAS sean minúsculas
print(cadena.count('t')) #Regresa cuantas a hay en la cadena
print(cadena.split('a')) #Enlistar y dividar mi cadena por cada 'a' que encuentre
print(cadena.upper(), cadena2.lower())
print(cadena.find('tardes')) #Me devuelve la posicion en la que encuentra "tardes", en caso de NO ENCONTRAR regresa -1

#Tuplas -> NO pueden ser modificadas
#Listas/Array en JS
tupla = (1, "HIJ", 10.3, False)
#tupla[0] = 2

#Listas / Arreglos
listaVacia = []
listaLlena = ["hugo", "paco", "luis"] #0 => hugo, 1 => paco, 2 => luis
print(listaLlena)
print(listaLlena[0])
listaLlena[0] = "donald"
print(listaLlena)
listaLlena.append('mickey') #Agregar un elemento al final de mi lista
print(listaLlena)
listaLlena.pop() #Elimina el último dato de mi lista
print(listaLlena)
listaLlena.pop(0) #Eliminamos el dato en la posición que ponemos entre paréntesis
print(listaLlena)
listaMix = ["String 1", 2, True, ["lista1.1", "lista1.2"]] #Lista/Arrays con más de un tipo de variable
print(listaMix)
nuevaLista = listaLlena + listaMix #Concatenando ambas listas
print(nuevaLista)

#Diccionarios -> Objeto en JS
dicionarioVacio = {}
diccionario = {"nombre": "Juan", "apellido:": "Perez", "edad": 18}
print(diccionario)
diccionario["estatura"] = 1.78
diccionario["hobbies"] = ["leer", "codificar", "jugar"]
print(diccionario)
diccionario.pop("edad")
print(diccionario)
estatura = diccionario.pop("estatura") #Elimina de mi diccionario, regresa el valor y asigna a variable estatura
print(estatura)
print(diccionario)
diccionario['estatura'] = estatura
print(diccionario)