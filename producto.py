class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio
        self.__mi_stock = {}

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio


    def actualizacion_de_stock(self):
        clave = self.__nombre
        valor = self.__precio
        self.__mi_stock[clave] = valor
        return self.__str__()

    def __str__(self):
        return ', '.join(f"{clave}: {valor}" for clave, valor in self.__mi_stock.items())

    def total_de_inventario(self):
        cantidad_claves = len(self.__mi_stock)
        return cantidad_claves


def main():

    nombre = ""
    precio = 0

    producto = Producto(nombre, precio)

    while True:
        nombre = input("Ingrese el nombre: ")
        if nombre.lower() == "salir":
            break
        precio = int(input("Ingrese el precio: "))

        producto.set_nombre(nombre)
        producto.set_precio(precio)
        producto.actualizacion_de_stock()
        print(f"Stock actualizado: {producto.actualizacion_de_stock()}")

    print(f"Antes de salir, teniamos ingresados los siguientes "
          f"Productos: {producto.actualizacion_de_stock()}")

    print(f"Total del inventario (Items): {producto.total_de_inventario()}")


if __name__=="__main__":
    main()



