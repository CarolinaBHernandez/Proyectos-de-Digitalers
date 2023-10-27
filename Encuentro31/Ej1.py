"""
Desarrollar un programa admin_alumnos.py que permita añadir, modificar, eliminar y listar los alumnos del servicio web.
Desarrollar menu de opciones

1 - Agregar
2 - Modificar
3 - Listar
4 - Eliminar
"""
import requests

def mostrar_menu():
    print("\nMENU DE OPCIONES:")
    print("1 - Agregar alumno")
    print("2 - Modificar alumno")
    print("3 - Listar alumnos")
    print("4 - Eliminar alumno")
    print("5 - Salir")

def agregar_alumno():
    name = input("Ingrese el nombre del alumno: ")
    courses = int(input("Ingrese la cantidad de cursos: "))
    response = requests.post("http://localhost:7001/student", json={"name": name, "courses": courses})
    print("Código de estado:", response.status_code)

def modificar_alumno():
    id = int(input("Ingrese el ID del alumno a modificar: "))
    name = input("Ingrese el nuevo nombre del alumno: ")
    courses = int(input("Ingrese la cantidad de cursos: "))
    response = requests.put(f"http://localhost:7001/student/{id}", json={"name": name, "courses": courses})
    print("Código de estado:", response.status_code)

def listar_alumnos():
    response = requests.get("http://localhost:7001/student")
    alumnos = response.json().get("students", [])

    print("Lista de alumnos:")
    for alumno in alumnos:
        print(f"ID: {alumno['id']}, Nombre: {alumno['name']}, Cursos: {alumno['courses']}")

def eliminar_alumno():
    id = int(input("Ingrese el ID del alumno a eliminar: "))
    response = requests.delete(f"http://localhost:7001/student/{id}")
    print("Código de estado:", response.status_code)

while True:
    mostrar_menu()
    opcion = input("\nElija una opción: ")

    if opcion == "1":
        agregar_alumno()
    elif opcion == "2":
        modificar_alumno()
    elif opcion == "3":
        listar_alumnos()
    elif opcion == "4":
        eliminar_alumno()
    elif opcion == "5":
        print("Bye")
        break
    else:
        print("Opción incorrecta.")
