from behave import given, when, then
from src.calculadora import Calculadora
import math

@given("que iniciei a calculadora")
def step_iniciar_calculadora(context):
    context.calc = Calculadora()
    context.exception = None
    context.resultado = None

# --- AÇÕES ---
@when("somo {a:d} e {b:d}")
def step_somar(context, a, b):
    context.resultado = context.calc.somar(a, b)

@when("subtraio {a:d} de {b:d}")
def step_subtrair(context, a, b):
    context.resultado = context.calc.subtrair(a, b)

@when("multiplico {a:d} por {b:d}")
def step_multiplicar(context, a, b):
    context.resultado = context.calc.multiplicar(a, b)

@when("divido {a:d} por {b:d}")
def step_dividir(context, a, b):
    context.resultado = context.calc.dividir(a, b)

@when("calculo a raiz quadrada de {a:d}")
def step_raiz(context, a):
    context.resultado = context.calc.raiz_quadrada(a)

@when('calculo a media dos numeros "{numeros_str}"')
def step_calcular_media(context, numeros_str):
    lista = [int(n) for n in numeros_str.split(",")]
    context.resultado = context.calc.media(lista)

# --- ERROS ---
@when("tento dividir {a:d} por {b:d}")
def step_tentar_dividir(context, a, b):
    try:
        context.calc.dividir(a, b)
    except Exception as e:
        context.exception = e

@when("tento calcular a raiz quadrada de {a:d}")
def step_tentar_raiz(context, a):
    try:
        context.calc.raiz_quadrada(a)
    except Exception as e:
        context.exception = e

# --- RESULTADOS ---
@then("o resultado deve ser {esperado:g}")
def step_verificar_resultado(context, esperado):
    assert math.isclose(context.resultado, esperado), \
        f"Esperado {esperado}, mas obtido {context.resultado}"

@then('devo receber um erro com a mensagem "{mensagem}"')
def step_verificar_erro(context, mensagem):
    assert context.exception is not None, "Era esperado erro, mas não ocorreu."
    assert str(context.exception) == mensagem, \
        f"Esperado erro '{mensagem}', mas obtido '{str(context.exception)}'"
