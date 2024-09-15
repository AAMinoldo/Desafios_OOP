class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def get_base(self):
        return self.__base

    def set_base(self, base):
        self.__base = base

    def get_altura(self):
        return self.__altura

    def set_altura(self, altura):
        self.__altura = altura

    def area_rectangulo(self):
        area = self.__base * self.__altura
        return area

    def perimetro_rectangulo(self):
        multiplo = 2
        perimetro = multiplo * (self.__base + self.__altura)
        return perimetro

def main():

    base = int(input("Ingrese un numero para la base: "))
    altura = int(input("Ingrese un nuero para la altura: "))

    rectantulo = Rectangulo(base, altura)

    rectantulo.perimetro_rectangulo()
    print(f"El perimetro es: {rectantulo.perimetro_rectangulo()}")


if __name__ == '__main__':
    main()