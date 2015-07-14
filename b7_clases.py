# B7- Clases, con más parámetros 


#1 CLASE - - - - - - - - - - - - - - - - 
class Personaje():

    # definicion
    def cabeza(self, posx):#self parametro de un metodo enel objeto
        fill(.3, .5, posx/300)
        oval(posx+10, 50, 80, 100)

    # definicion
    def saludar(self, posx, nombre):
        texto = "soy\n" + nombre
        fill(.2, .9)
        fontSize(20)
        textBox(texto, (posx-25, 60, 150, 80), align="center" )




#2 OBJETO - - - - - - - - - - - - - - - - 
cone = Personaje()
hulk = Personaje()

# luego se acceden a sus metodos
cone.cabeza(100)
cone.saludar(100, "Cone")

hulk.cabeza(300)
hulk.saludar(300, "Hulk")




#3 muchos Personajes...
for i in range(0, 20):
    hulk.cabeza(100*i)
    hulk.saludar(100*i, "Hulk"+str(i)    )
    