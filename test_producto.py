import pytest
from producto import Producto

@pytest.mark.parametrize("nombre, precio, resultado_esperado", [
    ("Remera", 20000,
     "Remera: 20000"),
    ("Buzos", 30000,
     "Buzos: 30000")
])
def test_de_actualizacion_de_stock(nombre, precio, resultado_esperado):
    my_producto = Producto(nombre, precio)
    assert my_producto.actualizacion_de_stock() == resultado_esperado


@pytest.mark.parametrize("nombre, precio, resulado_esperado",[
    ("Remera", 20000, 0)
])
def test_de_calculo_del_total_de_inventario(nombre, precio, resulado_esperado):
    my_producto = Producto(nombre, precio)
    assert my_producto.total_de_inventario() == resulado_esperado

@pytest.mark.parametrize("nombre, precio, resultado_esperado", [
    ("Remera", 20000, "Remera: 20000"),
    ("Buzos", 30000, "Buzos: 30000")
])
def test_str_imprime_datos_inventario(nombre, precio, resultado_esperado):
    my_producto = Producto(nombre, precio)
    my_producto.actualizacion_de_stock()#hay que llamar a este metodo, porque trabajan juntos
    resultado = str(my_producto)
    assert resultado == resultado_esperado
