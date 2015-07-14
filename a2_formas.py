## A2- Ejercicio 2: dibujar formas básicas (rect, oval, colores)

## El punto 0,0 está abajo a la izquierda. 


#1 rectangulo gris
fill(.5) # color rgb y alpha, rango de 0 a 1, tambien cmyk
rect(0, 0, 100, 100) # orden de los argumentos pos x, pos y, ancho, alto



#2 círculo amarillo 
fill(.9, .9, .0) # rgb y alpha, 0 a 1
oval(50, 250, 200, 200) # circulos pos x, pos y, ancho, alto



#3 círculo rojo
fill(1.0, .0, .0, .7) # rgb y alpha, 0 a 1
oval(50, 200, 200, 100) # pos x, pos y, ancho, alto



#4 línea verde 
stroke(.0, .9, .0)
strokeWidth(10)
line((300, 100), (300, 500))



#5 polígono azul 
fill(0, .0, .9, .9) # rgb y alpha, 0 a 1
stroke(0, .5)
# 1er, 2do, 3er y 4to punto, close para cerrar o no el contorno
polygon((400, 300), (400, 500), (700, 600), (520, 250), close=True)