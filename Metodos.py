
def nome_funcion (parametro1, parametro2):
    print(parametro1, parametro2)

nome_funcion(1, 2)

def suma (a , b : int):
    return a + b

print(suma(1, 2))

def concatenar (a, b: str):
    return a + b

print(concatenar("Hola", " Mundo"))
print(concatenar(1, 2))
print(concatenar('1', '2'))

## Parametros por defecto
def saudar (nome = "Mundo"):
    print("Ola", nome)

saudar()
saudar("Pepe")

## Metodos con parametros indeterminados

def varios_parametros (parametro1, parametro2, *otros):
    print(parametro1)
    print(parametro2)
    print(otros)

varios_parametros(1, 2, 3, 4, 5)

def suma_varios (*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

print(suma_varios(1, 2, 3, 4, 5))

def varios_parametros_non_anonimos (parametro1, parametro2, **otros):
    print(parametro1)
    print(parametro2)
    print(otros)

varios_parametros_non_anonimos(1, 2, terceiro = 3, cuarto = 4, quinto = 5)

## podense retornar varios valores
def varios_valores ():
    return 1, 2, 3, 4, 5
a, b, c, d, e = varios_valores()

print(a, b, c, d, e)
