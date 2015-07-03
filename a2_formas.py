## A2- Ejercicio 2: dibujar formas básicas (rect, oval, colores)

## el 0, 0 esta abajo a la izquierda. 

fill(.5) # rgb y alpha, 0 a 1
rect(0, 0, 100, 100) # pos x, pos y, ancho, alto

fill(.1, .4, .6, .5) # rgb y alpha, 0 a 1
oval(50, 250, 100, 100) # pos x, pos y, ancho, alto

fill(.1, .4, .6, .3) # rgb y alpha, 0 a 1
oval(50, 200, 100, 100) # pos x, pos y, ancho, alto





stroke(0)
line((0, 200), (300, 200))

stroke(0, 0)
polygon((300, 300), (300, 500), (500, 500), (420, 280), close=True)