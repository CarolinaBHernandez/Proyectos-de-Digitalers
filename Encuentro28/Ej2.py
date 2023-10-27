"""1) Crear una clase Persona que sea la clase padre de otra que se llame Estudiante

La clase Persona, en su método __init__() debe estar preparada para recibir nombre y apellido. 
Además esta clase debe tener un método para mostrar nombre_completo() el cual debe mostrar por pantalla
el nombre acompañado del apellido.

La otra clase "Estudiante" debe poder heredar de Persona y además recibir los argumentos nombre y edad.
También la clase Estudiante recibe el valor carrera y debe contar con un método mostrar_carrera()."""


class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def nombre_completo(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"

class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido)  
        self.edad = edad
        self.carrera = carrera

    def mostrar_carrera(self):
        return self.carrera



estudiante1 = Estudiante("Carolina", "Hernández", 30, "Programación")
print(estudiante1.nombre_completo())
print(f"Edad: {estudiante1.edad}")
print(f"Carrera: {estudiante1.mostrar_carrera()}")
