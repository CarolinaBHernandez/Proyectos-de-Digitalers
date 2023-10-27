"""1) Crear una clase "Persona" con atributos nombre y edad
2) Crear un método cumpleanios() que aumente en 1 la edad de la persona cada vez
que se ejecute ese método.
3) Imprimir por pantalla de manera formateada un saludo que incluya el nombre y la edad"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def cumpleanios(self):
        self.edad += 1
        print(f"Soy {self.nombre} y ahora tengo {self.edad} años.")

aumentar_edad = Persona("Carolina", 30)
aumentar_edad.cumpleanios()
