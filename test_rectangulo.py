import pytest
from rectangulo import Rectangulo


@pytest.mark.parametrize("base, altura, resultado", [
    (10, 20, 200)
])
def test_area_de_un_rectangulo(base, altura, resultado):
    my_rectangulo = Rectangulo(base, altura)
    assert my_rectangulo.area_rectangulo() == resultado


@pytest.mark.parametrize("multiplo, base, altura, resultado", [
    (2, 10, 20, 60)
])
def test_perimetro_de_un_rectangulo(multiplo, base, altura, resultado):
    my_rectangulo = Rectangulo(base, altura)
    assert my_rectangulo.perimetro_rectangulo() == resultado
