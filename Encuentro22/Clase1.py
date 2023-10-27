"""
PYTHON 
------
"""

enteros =10
punto_flotante = 5.8
cadenas ="Hola"
booleanos = True
complejos = 2 + 6j #consultar libreria CMATH

#Casting - convertir una variable de un tipo a otro

a= 10
b= 2.5
resultado = a + b
print (resultado)
print(type(resultado))


#Colecciones

#lista = [1, 2, 3, 4, 5]
      #  0  1  2  3  4
      # -5 -4 -3 -2 -1  

#print(lista [2])

animales = ['perro', 'gato', 'conejo', 'hamster', 'vaca', 'leon']
#print(animales[2:5]) #SLICES --> ['conejo', 'hamster', 'vaca']

#print(animales[0:5:2]) # El tercer parametro es el paso al que reproduce la secuencia (de 2 en 2) ['perro', 'conejo', 'vaca']

lista=[10, 5.4, False, ["otra lista", True]]
#print(lista[1])
#print(lista[3])
#print(lista[3][0])

#lista[2] = "Hola"
#print(lista)

lista.append('otro elemento') # --> [10, 5.4, False, ['otra lista', True], 'otro elemento']
lista.insert(1, 12) # --> [10, 12, 5.4, False, ['otra lista', True], 'otro elemento']
print(lista)

#TUPLAS

tupla = (1, 2, 3, 4)

un_elemento = (5,) #Ponerle la , para que python lo tome como tupla
print(type(un_elemento))

#DICCIONARIOS

diccionario = {'a' : 1, 'b':2}
print(diccionario['b'])

diccionario2 = {1:'uno', 2 :'verdadero', (1,2) :tupla, False: 'dos'}

diccionario2[1] = '1' #Modifica un elemento
diccionario2[3] = '3' #Crea un elemento al final del diccionario
del diccionario2[3] #Elimina un elemento a traves de su key
print(diccionario2)
#print(diccionario[(1,2)])

#SET, FROZEN SET

lista_repetida = [1, 2 , 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 7, 7, 7, 8, 8 ]
set1 = set(lista_repetida)
print(set1) # --> {1, 2, 3, 4, 5, 6, 7, 8}

#FROZEN SET --> Una vez definido no se puede modificar

frutas= frozenset(['manzana', 'banana', 'cereza'])

#len() y del

#con del elimino elementos, con len() conozco la longitud de una coleccion
#print(len(lista_repetida))

#UNPACKING - desempaquetado
#Asingno elementos de una tupla o listas o variables

#a, b, c, d = tupla

#print(a, b, c, d)

#OPERADORES ARITMETICOS

suma = 5 + 6
resta = 10 - 2
multiplicacion= 2 * 4
division = 10 / 2
modulo = 9 % 2
exponencial = 2 ** 3
division_entera= 9 // 2


#OPERADORES RELACIONALES

x = 5

x == 6 #Evalua igualdad - False
x != 8 #Evalua diferencia - True
x > 4 #True
x < 3 #False
x >= 20 #False
x <=5 #True

#OPERADORES LOGICOS

x == 6 and x == 5 #Devuelve true si ambos elementos son true.
x == 6 or x == 5 #Devuelve true si al menos un elemento es true.
not x > 4 #Devuelve el contrario. Si a era True me devuelve False y viceversa. 

#OPERADOR DE IDENTIDAD (is)

a = 10
b = 10 

print(id(a), id(b)) # --> 140708168131656 140708168131656

print(a is b)

a is b #Devuelve True ya que apuntan a la misma direccion de la memoria.

#OPERADOR DE MEMBRESIA

datos = [1, 2, 3]
print(3 in datos) #Devuelve True porque 3 es miembro de datos.
print(10 in datos)#Devuelve False porque 10 no es miembro de datos.


#OPERADOR WALRUS (MORSA) :=
#Simplifica la operacion de asignacion. Crea una variable, le asigna un valor y la ejecuta

#dato = "hola"
#print(dato)

#print(dato:="Hola")
#print(dato)

#SENTENCIAS DE CONTROL
#Resultado de evaluacion exitosa -condicion - else - resultado de evaluacion no exitosa.
"""
nombre = "Juan"

if nombre == 'Pedro':
    print("Tu nombre es Pedro")
else:
    print('Tu nombre no es Juan,sino' +nombre)

"""
edad = 19

print("La edad es de 18 años" if edad == 18 else "La edad no es de 18 años sino " +str(edad))

#ELIF
"""
edad = 80

if edad < 18:
    print("Sos menor de edad")
elif edad > 65 :
    print("Sos mayor de edad")
else:
    print("Ya estas jubilado")  
"""
"""
numero = 0

if numero:
    print('El numero es ' str(numero))
else:
    print('Falso, el numero es 0')

"""

#BUCLE WHILE

a = 1

while a < 3 :
    print(a)
    a += 1

#BUCLE FOR

datos = [1, 2, 3, 4]

#for dato in datos:
#    print(dato)

#BREAK Y CONTINUE

#BREAK
"""
contador = 0

while True:
    print("Este es el paso", contador)
    contador += 1

    if contador >=5:
        print("La condicion se cumple, salimos del bucle")
        break
"""
#CONTINUE
"""
contador = 0

while contador < 5:
    contador +=1

    if contador == 3:
        print("Saltando la iteracion cuando contador sea 3")
        continue
    print("Este es el paso ", contador)
"""
#FUNCIONES BUILT- IN

#print() input() range()

#A range le puedo pasar hasta 3 parametros, el primero es el inicio de la secuencia, el segundo es el final de la secuencia
# el cual ese mismo numero es excluido, y el tercer parametro es el paso de la secuencia (ej de 2 en 2)
for numero in range (2, 10, 2):
    print(numero)

lista_pares =list(range (2,11,2))
print(lista_pares)

#int(), float(), str(), len(), min(), max(), bool()

#FUNCIONES

"""def nombre_funcion(argumento, argumento2):
    #BLOQUE DE CODIGO"""

def sumar(a,b):
    c = a+b

print(sumar(10,20))

def imprimir_mensajes(mensaje = "No se escribio nada"):
    """Esta funcion sirve para imprimir mensajes,
       si no se le pasa ningun parametro, devolvera un mensaje
       por defecto.
    """
    print(mensaje)
    
    help(imprimir_mensajes)
    #imprimir_mensajes()

#SCOPE

x = 1

def funcion():
    global x
    x = 2
print(x)
print(funcion)
print(x)


def funcion_externa():
    z= "hola"

    def funcion_interna():
        nonlocal z
        z= "chau"

    funcion_interna()
    print(z)


#ARGUMENTOS DE LONGITUD VARIABLE

def funcion(*args):
    #print(type(args))
    #print(args)
    pass

#funcion(1, 2, 3, 4, 5, 6, 7)

def suma(**kwargs):
    #print(type(kwargs))
    #print(kwargs)

    total = 0
    for arg in kwargs:
        total += kwargs[arg]
    #print(total)

    suma(a=10, b=20, c=30, d=40, e=77)

#ORDEN DE LOS ARGUMENTOS DE LAS FUNCIONES

def funct(a, b, *args, c='hola', **kwargs ):
    pass

