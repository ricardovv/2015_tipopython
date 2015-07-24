# A3- Ejercicio 3: dibujar texto

"""
#1
fill(1, 1, 0)
rect(100, 50, 300, 300)

fill(0)
fontSize(30)
lineHeight(50)
# el texto escrito directamente entre comillas
textBox("Les gusta python?", (100, 50, 300, 300), align="left")
"""


#2
fontSize(30)
lineHeight(50)

lindo = "es lindo el perro"

feo = "es muy feo el perro"

# usamdo variables, cambian feo o lindo, y cambia lo que muestra la consola
textBox(feo, (500, 50, 300, 300), align="left")

