# B6- Clases
# una clase es como un modelo de algo, 
# como un "timbre" o "molde" 
# tiene dos partes,  la "Clase" y el "Objeto"    
# como un molde para hacer galletas y la galleta

# CLASE - - - - - - - - - - - - - - - - 
# la clase "define" un objeto y sus caracteristicas, pero no "existe"
# tiene datos y metodos
class Personaje():

    # definicion
    def cabeza(self):#self parametro de un metodo enel objeto
        fill(.4, .5, .8)
        oval(posx+10, 50, 100, 120)

    # definicion
    def saludar(self):
        fill(.2, .9)
        fontSize(24)
        textBox("Hola", (30, 100, 150, 50) )


# OBJETO - - - - - - - - - - - - - - - - 
# Hace que el "objeto" exista
# primeto se asigna a una variable
cone = Personaje()
hulk = Personaje()

# luego se acceden a sus metodos
cone.cabeza()
cone.saludar()
