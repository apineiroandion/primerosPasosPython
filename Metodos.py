
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


