# While
repeticiones = 5
while repeticiones > 0:
    print (repeticiones)
    repeticiones -= 1

# Do while
repeticiones = 5
while True:
    print (repeticiones)
    repeticiones -= 1
    if repeticiones == 0:
        break

# For
for i in range(5):
    print (i)

print("")

for i in range(5, 10):
    print (i)

print("")

for i in range(0, 10, 2):
    print (i)

print("")

for i in range(10, 0, -1):
    print (i)

print("")

# For con listas
lista = [1, 2, 3, 4, 5]
for i in lista:
    print (i)

print("")

lista2 = [1, "Dous", 3.0, [4, "V"]]
for i in lista2:
    print (i)

print("")

for i in range(len(lista2)):
    print (lista2[i])

print("")

for i, elem in enumerate(lista2):
    print (i, elem)
print("")

for i, elem in enumerate(lista2):
    if i%2 == 0:
        print (i, elem)
print("")

# For con diccionarios
diccionario = {'a': 1, 'b': 2, 'c': 3}
for i in diccionario:
    print (i)
print("")

for i in diccionario:
    print (diccionario[i])
print("")

for i in diccionario:
    print (i, diccionario[i])
print("")

for clave, valor in diccionario.items():
    print (clave, valor)
print("")

for i in enumerate(diccionario):
    print (i)
print("")


