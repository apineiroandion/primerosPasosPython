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