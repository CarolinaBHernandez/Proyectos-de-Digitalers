"""Utilizando un bucle While elaborar un codigo que imprima en pantalla cada uno de los elementos de una lista 
y simultáneamente los elimine, hasta quedar vacía"""



lista = [1, 2, 3, 4, 5]


while lista:
    
    print(lista[0])
    
    del lista[0]

print(lista)




