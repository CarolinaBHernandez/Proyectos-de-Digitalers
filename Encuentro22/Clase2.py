#FUNCIONES DE ORDEN SUPERIOR

def sumar(x):
    return x + 10 

def cuadrado(x):
    return x ** 2

def superior(funcion, lista):
    resultado = []
    for num in lista:
        resultado.append(funcion(num))
    return resultado
    
numeros = [2, 5, 10]
#print(superior(sumar, numeros))
#print(superior(cuadrado, numeros))


#FUNCIONES LAMBDA

lambda x : x + 10
lambda x : x ** 2

#print(superior(lambda x : x + 10, numeros ))
#print(superior(lambda x : x ** 2, numeros ))

#EXCEPCIONES
"""
try:
    int('Hola')
except ValueError:"El argumento no es un número"
except NameError:
    print("Ese no es el nombre")
except TabError:
    print("No es el tab")
except Exception:
    print("El argumento no es un número")
else: 
    print("Todo salió bien")
finally:
    print("Se terminó el bloque")
"""

#OPERACIONES CON STRINGS 

texto = "\tEjemplo de caracteres especiales    " # \t tabulado, \n salto de linea.
#print(texto[2:]) #Slicing
#print(texto * 2)
#print(texto.startswith("Ejemplo")) #Valida con que caracteres comienza el texto.
#print(texto.endswith("especiales"))  #Valida con que caracteres termina el texto.
#print(texto.strip) #Quita espacios iniciales y finales.
#texto = texto.replace("especiales", "espaciales") #Remplaza una cadena de texto por otra.
#texto = texto.split(',') #Crea una lista con elementos delimitado por comas
#print(texto.find("caracteres")) #Busca y devuelve el inidice donde se encuentra la primer letra buscada.
#print(texto.upper())#Devuelve todo el texto en mayusculas.
#print(texto.lower())#Devuelve todo el texto en minusculas.
#print(texto.capitalize())#Devuelve en mayuscula la primer letra del texto.


#FORMACION DE CADENAS
"""
edad = 20
print("Juan tiene " +str(edad) + " años")
#---------------------------------------
#Nº1
nombre = "Juan"
edad = "20"
mensaje = "Hola, me llamo {0}, y tengo {1} años"
print(mensaje.format(nombre,edad))

#Nº2
nombre = "María"
edad = "30"
mensaje= f"Hola, me llamo {nombre} y tengo {edad} años"
print(mensaje)
"""

#ENTRADA Y SALIDA DE ARCHIVOS

#WITH


#with expresion as variable:
    #Bloque de codigo

#Parámetros de open()---> "w"(para write/ escritura), "r"(read/lectura), "a"(append/agregar)

"""
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, aca estoy!")

with open("archivo.txt", "a") as archivo:
    archivo.write("\n Seguimos agregando contenido")

with open("archivo.txt", "r") as archivo:
    print(archivo.read())
"""
"""
archivo = open("archivo.txt", "r")
print(archivo.read())
print(archivo.readline())
archivo.close()
"""
"""
texto = ["Primera linea\n", "Segunda linea\n", "Tercera linea\n"]
archivo = open("archivo2.txt", "w")
archivo.writelines(texto)
archivo = open("archivo2.txt", "r")
print(archivo.read())
archivo.close()
"""
"""
texto = ["Primera linea\n", "Segunda linea\n", "Tercera linea\n"] 
archivo = open("archivo2.txt", "r+")
archivo.writelines(texto)
archivo.seek(0)
print(archivo.read())
archivo.close()
"""
"""
with open ("archivo2.txt","r+") as archivo:
    texto = ["Primera linea\n", "Segunda linea\n", "Tercera linea\n"] 
    archivo.writelines(texto)
    archivo.seek(0)
    print(archivo.read())
"""
 