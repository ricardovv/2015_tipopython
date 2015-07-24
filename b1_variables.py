## B1- Guardar Datos: Variables, tipos datos, suma, print, str(), int()
# Variable sirven para guardar y reusar datos
# Tipos de datos: 1, 5.4, "Hola" son tipos de datos diferentes
# 1 es un int (número entero)
# 5.4 es un float (número de punto flotante) 
# "Hola" es String (una cadena de caractéres) 

# Diferentes tipos de datos se almacenan de diferente manera en la memoria del computador, no pueden mezclarse (mentira, si se puede, pero con unos trucos...)

# Pasos para trabajar con variables
# a-se declaran: con un nombre
# b-se les asigna un valor: con igual =
# c-se usan: colocandolo donde queramos usar su valor


#1
a = 10         # int, datos enteros: 0, 5, -27, 1000
b = 5.5        # float, datos de punto flotante: 4.6, 3.1416,  -5.2

resultado = a + b
texto = "El resultado es:" # string, una cadena de caracteres

print texto, resultado # "concatenar" texto y el resultado en una línea, separar con coma




"""
#2 como los datos de distinto tipo no pueden mezclarse, 
# a veces es necesario convertirlos de un tipo a otro 
print float(a), int(b), int("7")
"""



"""
#3 Concatenar v/s sumar (u otra operación)
#print 2 + 2 # entre numeros, el signo + suma
print "2" + 2 # esto no funciona, uno es un string y otro es número
"""


