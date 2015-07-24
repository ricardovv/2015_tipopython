# B5- Reusar: Funciones 
# una funcion es una especie de timbre, que puede ser reutilizado
# Cambiando algunos valores


# se definen sus propiedades, y se usa ingresando nuevos valores, si corresponde



# 1
#a definición de la función y lo que hace: 
#en este caso solo print una  palabra que se le entregará
def mynombre(nom):
    print nom
    
# uso: 
# el valor que se coloca entre paréntesis "entra" hacia print nom en la definición:
mynombre("hi")     
mynombre("chao")




# 2
# b definición
def caja(nombre, edad, posx):
    fill(.9, .2, edad/200) # color de las barras
    rect(posx, 100, 98, edad*5) # las barras
    fill(.2, .9) # color del texto 
    fontSize(24) # tamaño de la fuente
    textBox(nombre, (posx, 50, 150, 50) ) # se dibuja la caja de texto
 
    
# se utiliza la funcion y se le dan distintos valores
# los valores "entran" y son pasados a su lugar
caja("juan", 65, 100)     
caja("maria", 25, 200)     
caja("pedro", 125, 300)     
caja("alicia", 50, 400)     

 

