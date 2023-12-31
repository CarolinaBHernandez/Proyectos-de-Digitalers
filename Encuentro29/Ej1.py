"""Desarrollar un programa que cree una base de datos SQLITE3 llamada productos.sqlite y una tabla de nombre productos con las siguientes columnas.

Columna	Tipo de Dato
id	NUMERIC
nombre	TEXT
precio	NUMERIC 


Luego el programa debe insertar las siguientes filas

id	nombre	precio
1	Teclado	25
2	Mouse	18
3	Monitor	300
4	Pad	100

"""

import sqlite3
import sys

dir = "C:\\Users\\User\\Desktop\\Python Digitalers\\It\\Encuentro29\\"

conn = sqlite3.connect(dir + "productos.sqlite")

cursor = conn.cursor()

try:
    cursor.execute("CREATE TABLE productos (id NUMERIC, nombre TEXT, precio NUMERIC)")
except sqlite3.OperationalError:
    print("La tabla ya existe!!")


cursor.execute("INSERT INTO productos VALUES(?, ?, ?)", (1, "Teclado", 25))
cursor.execute("INSERT INTO productos VALUES(?, ?, ?)", (2, "Mouse", 18))
cursor.execute("INSERT INTO productos VALUES(?, ?, ?)", (3, "Monitor", 300))
cursor.execute("INSERT INTO productos VALUES(?, ?, ?)", (4, "Pad", 100))


#conn.commit()
#conn.close()



"""Realizar un programa que permita agregar nuevos productos a la base anterior a través de la consola.
 Se debe solicitar para cada producto un id (numerico), un nombre (texto) y un precio (numérico). 

Menu
1 - Agregar Productos
2 - Ver productos
3 - Salir

La opcion 1 despliega la entrada de datos
La opcion 2  muestra los productos de la tabla
La 3 nos permite salir del programa (sys.exit())"""


def menu():
    print("\nMenu:")
    print("1 - Agregar productos")
    print("2 - Ver productos")
    print("3 - Salir")

def agregar_productos():
    id_producto = int(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))

    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    existente = cursor.fetchone()

    if existente:
        print("El producto ya existe en la base de datos.")
    else:
        cursor.execute("INSERT INTO productos (id, nombre, precio) VALUES (?, ?, ?)", (id_producto, nombre, precio))
        conn.commit()
        print("El producto se ingresó con éxito!")


def listar_productos():
    cursor.execute("SELECT * FROM productos")
    productos_db = cursor.fetchall()

    if productos_db:
        print("\nProductos en la base de datos:")
        for producto in productos_db:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}")
    else:
        print("\nNo hay productos en la base de datos.")
    
while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_productos()
    elif opcion == "2":
        listar_productos()
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción incorrecta. Por favor, selecciona una opción válida.")

conn.close()
sys.exit()
