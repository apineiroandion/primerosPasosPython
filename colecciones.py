# Colecciones en Python

#Lista
l = [1, 2, 3, 4, 5]
print (l[3])

l2 = list() #Crea unha lista valeira
print (type (l2))

l3 = [1, "Dous", 3.0, [4, "V"], 4]
print (l3[1][1])
print (l3[3][1])
print (l3[-2])
print (l3[1:3])
print (l3[1:5:2]) #Saltos de 2 en 2
l3[4] = 'Seis'
print (l3)
l3[1:3] = [2, 3]
print (l3)

##Tuplas
t = (1, 2, 3, 4, 5)
print (t[3])
print (type(t))
t2 = tuple() #Crea unha tupla valeira
print (type(t2))
t3 = (1, "Dous", 3.0, [4, "V"], 4)
print (t3[1][1])
print (t3[3][1])
print (t3[-2])
print (t3[1:3])
print (t3[1:5:2]) #Saltos de 2 en 2
#t3[4] = 'Seis' #Non se pode modificar unha tupla
#para crear una tupla de un elemento se pone la coma
t4 = (1,)
print(type(t4))

## Diccionarios
d = {'a': 1, 'b': 2, 'c': 3}
print (d['a'])
print (d)
print (type(d))
d2 = dict() #Crea un diccionario valeiro
print (type(d2))
d3 = {'a': 1, 'b': "Dous", 'c': 3.0, 'd': [4, "V"], 'e': 4}
print (d3['b'][1])
print (d3['d'][1])
d3['f'] = 'Seis'
print (d3)
d3['b'] = 'Dous'
print (d3)

##Sentencias Condicionais
# if (importante el sangrado)
variable = 3
if variable == 5:
    print ("A variable é 5")
else:
    print ("A variable non é 5")

# operador ternario
variable = 5
print ("A variable é 5" if variable == 5 else "A variable non é 5")
par = True if variable % 2 == 0 else False
print(par)