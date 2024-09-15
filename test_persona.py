import pytest
from persona import Persona

@pytest.mark.parametrize("nombre, edad, DNI, resultado_esperado",[
    ("Aldo", 55, 20873426,
     "Nombre: Aldo, Edad: 55, DNI: 20873426")
])

def test_str_imprime_datos(nombre, edad, DNI, resultado_esperado):
    my_persona = Persona(nombre, edad, DNI)
    resultado = str(my_persona)
    assert resultado == resultado_esperado

@pytest.mark.parametrize("valor, resultado",[
    (18, True),
    (16, False)
])
def test_es_mayor_de_edad(valor, resultado):
    my_persona = Persona("Aldo", valor, DNI=20873426)
    assert my_persona.es_mayor_edad() == resultado

