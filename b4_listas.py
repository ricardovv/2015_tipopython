# B4- Colección de Datos: Arrays y loops
# Arrays es una lista de variables, una colección de datos

# como las variables, se declaran, se asignan valores, se usan
# tienen valores y posición (o index)
# la posición inicial es 0, NO 1 


 
#1 arrays de un mismo elemento o tipo de datos
iguales = [1, 50, 45, -4]
print iguales




"""
#2 arrays de diversos elementos o tipos de datos
diversos = [1, 50, "hola", (10, "dos")]
print diversos
"""



"""
#3 Acceder a uno de los valores
personajes = ["Godzila", "Ultraman", "Mazinger"]
#print personajes[3] # entre braqckets el index

# mono pasa por todos los personajes: "para cada mono en la lista personajes"
for mono in personajes:
    #print mono
    print personajes[2]
""" 


"""
#4 agrupar y representar datos
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

