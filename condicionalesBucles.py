#Condicionales
x = 20
if x > 10:
    print("Número mayor a 10")
    print("Otra impresion")
    print("Tercera impresion")
else:
    print("Menor a 10")

if x > 10:
    print("Mayor 10")
elif x > 15:
    print("mayor 15")
else :
    print("menor a 10")


#Bucles
for  x in range(5): #Del 0 al 4. YA NO entra en 5
    #Codigo
    print(x)

for y in range(1, 5): #Comenzando de 1 hasta 4. No entramos en 5
    print(y)

for z in range(0, 10, 2): #Comenzando en 0 hasta 10, avanzando de 2 en 2
    print(z)

array = ['A', 'B', 'C', 'D']
#Obtener la posicion
for i in range(0, len(array)):
    print(i, array[i])

for v in array: #Foreach en Js
    print(v)

diccionario = {"nombre": "Jose", "apellido": "Doe", "edad": 19}
for k in diccionario: #Por cada atributo/llave del diccionario
    print(k, diccionario[k])


#WHILE
y = 0
while y < 3:
    print(y)
    y += 1
else:
    print("Sentencia else", y)

#BREAK -> interrumpir completamente mi ciclo/bucle.
for x in range(16):
    if x == 13:
        break
    print(x)

#Continua -> interrupción temporal. SOLO no me lo ejecuta en esa ronda del bucle
for x in range(16): 
    if x == 13:
        continue
    print(x)

#Ejercicio
#Dado el for 1 al 15, imprime todos los numeros EXCEPTO aquellos múltiples de 5
for x in range(1, 16):
    if x % 5 == 0:
        continue
    print(x)

string = "Buenos días"
for x in string:
    print(x)

#Dada una cadena, imprima cada uno de los caracteres y que se detenga POR COMPLETO si encuentra un . (PUNTO)
cadena = "Hola, buenos días. Cómo estás?"
for y in cadena:
    if y == ".":
        break
    print(y)
