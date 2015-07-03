# B5- Reusar: Funciones 
# una especie de timbre, que puede ser reutilizado,
# Cambiando algunos valores
#definirla, usarla

# definicion
def mynombre(nom):
    print nom
    
# uso, el valor entra
mynombre("hi")     
mynombre("chao")



# definicion
def caja(nombre, edad, posx):
    fill(.9, .5, edad/90)
    rect(posx, 100, 98, edad*5)
    fill(.6, .9)
    fontSize(24)
    textBox(nombre, (posx, 50, 150, 50) )


    
# uso, el valor "entra" y es pasado a su lugar
caja("juan", 55, 100)     
caja("maria", 25, 200)     
caja("pedro", 75, 300)     


