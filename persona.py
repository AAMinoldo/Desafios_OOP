class Persona:
    def __init__(self, nombre, edad, DNI):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

    def get_DNI(self):
        return self.__DNI

    def set_DNI(self, DNI):
        self.__DNI = DNI

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__DNI}"

    def es_mayor_edad(self):
        if self.__edad >= 18:
            return True
        else:
            return False

def main():
    print("Bienvenidos al sistema de evaluacion de edad")

    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    DNI = int(input("Ingrese Dni: "))

    persona = Persona(nombre, edad, DNI)

    print("\nInformación de la Persona:")

    if persona.es_mayor_edad():
        print("La persona es mayor")
    else:
        print("La persona es menor")


if __name__=="__main__":
    main()
