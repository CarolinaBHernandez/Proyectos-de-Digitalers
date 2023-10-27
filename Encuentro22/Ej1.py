"""Crear un bucle que almacene en una variable la suma de todos los elementos numéricos de una lista
 con excepción del último elemento."""


lista = [10, 2, 5, 8, 7]

suma = 0

for num in lista[:-1]:
    suma += num

print("La suma de los números excepto el último es:", suma)
