#Tenemos una lista de personas
lista = ["juan salvo", "henry courtney", "elizabeth bennet", "marge simpson"]
#Crear una funcion que ponga mayúscula solo en la primer letra,
# tanto del nombre como del apellido y devuelva otra lista con estos cambios.

def capitalizar(lista):
    resultado= []

    for nombre in lista:
        
        nombre_apellido = nombre.split()
        if len(nombre_apellido) == 2:
            nombre, apellido = nombre_apellido
            nombre = nombre.capitalize()
            apellido = apellido.capitalize()
            nombre_capitalizado = f"{nombre} {apellido}"
            resultado.append(nombre_capitalizado)

    return resultado

lista = ["juan salvo", "henry courtney", "elizabeth bennet", "marge simpson"]

resultado = capitalizar(lista)

print(resultado)


"""
lista = ["juan salvo", "henry courtney", "elizabeth bennet", "marge simpson"]

i=0
for cad in lista:
    lista[i]= lista[i].title()
    i+=1
print(lista)"""
