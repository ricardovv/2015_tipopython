# B7- Clases

# CLASE - - - - - - - - - - - - - - - - 
class Personaje():

    # definicion
    def cabeza(self, posx):#self parametro de un metodo enel objeto
        fill(.3, .5, posx/300)
        oval(posx+10, 50, 100, 120)

    # definicion
    def saludar(self, posx, nombre):
        texto = "Hola, \nsoy " + nombre
        fill(.2, .9)
        fontSize(22)
        textBox(texto, (posx+10, 70, 150, 80), align="center" )


# OBJETO - - - - - - - - - - - - - - - - 
# Hace que el "objeto" exista
# primeto se asigna a una variable
cone = Personaje()
hulk = Personaje()

# luego se acceden a sus metodos
cone.cabeza(100)
cone.saludar(100, "Cone")


hulk.cabeza(300)
hulk.saludar(300, "Hulk")
