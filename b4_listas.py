# B4- Colección de Datos: Arrays y loops

# Arrays es una lista de variables, una coleccion de datos
# se declara, se asignan valores, se usan
# tiene valor 
# y posicion o index, posicion inicial es 0, NO 1

#a- de un mismo elemento o tipo de datos
iguales = [1, 50, 45, -4]
print iguales


#b- de diversos elementos o tipos de datos
"""
diversos = [1, 50, "hola", (10, "dos")]
print diversos
"""


"""
#c- Acceder a uno de los valores
personajes = ["Godzila", "Ultraman", "Mazinger"]
#print personajes[3] # entre braqckets el index

# por todos los personajes: "para cada uno en la lista"
for mono in personajes:
    print mono
"""


"""
#d- agrupar y representar datos
nombre  = ["juan", "maria", "alicia", "pancho", "lucho"]
edad     = [30, 45, 16, 28, 87]
largo = len(nombre) # cantidad de elementos

for i in range(0, largo):
    posx = 200+100*i
    print "la edad de", nombre[i], "es", edad[i] 
    fill(.2*i, .4, .2)
    rect(posx, 200, 98, edad[i]*5)
    fill(0)
    fontSize(20)
    textBox(nombre[i], (posx, 170, 200, 30) )
"""    
    
    