# B6- Clases
# una clase es como un modelo de algo, 
# como un "timbre" o "molde", preo mas complejo que una función 
# tiene dos partes,  la "Clase" y el "Objeto"    
# como un molde para hacer galletas (clase) y la galleta (objeto)



#1 CLASE - - - - - - - - - - - - - - - -
# definición de la clase. 
# Se "define" una clase y sus características, pero esta clase no "existe"
# tiene datos y métodos (o funciones)

class Personaje():
    # definición de la cabeza
    def cabeza(self):#self parámetro de un método en el objeto
        fill(.4, .5, .8)
        oval(10, 50, 100, 120)

    # definición de la acción de saludar
    def saludar(self):
        fill(.2, .9)
        fontSize(24)
        textBox("Hola", (30, 100, 150, 50) )


#2 OBJETO - - - - - - - - - - - - - - - - 
# Hace que el "objeto" exista
# primero se asigna a una variable
# nombreVariable = NombreClase() 
cone = Personaje() # cone será una cariable del tipo Personaje 
hulk = Personaje() # hulk será una cariable del tipo Personaje 


# usando notación de punto (.) se accede a sus métodos, o lo que hace la clase
cone.cabeza()
cone.saludar()

# problema, todos comparten las mismas propiedades
# como variar sus parámetros?
hulk.cabeza()
hulk.saludar()


