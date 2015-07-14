# B6- Clases
# una clase es como un modelo de algo, 
# como un "timbre" o "molde" 
# tiene dos partes,  la "Clase" y el "Objeto"    
# como un molde para hacer galletas y la galleta



#1 CLASE - - - - - - - - - - - - - - - -
# definición de la clase. Se "define" una clase y sus características, pero esta clase no "existe"
# tiene datos y métodos
class Personaje():

    # definición
    def cabeza(self):#self parámetro de un método en el objeto
        fill(.4, .5, .8)
        oval(10, 50, 100, 120)

    # definición
    def saludar(self):
        fill(.2, .9)
        fontSize(24)
        textBox("Hola", (30, 100, 150, 50) )




#2 OBJETO - - - - - - - - - - - - - - - - 
# Hace que el "objeto" exista
# primeto se asigna a una variable
cone = Personaje()
hulk = Personaje()


# luego se acceden a sus métodos usando notación de punto (.)
# problema, tyodos comoarten las mismas propiedades
cone.cabeza()
cone.saludar()

# hulk.cabeza()

