# B8, CLASES
# Ejemplo basado en ejemplo de Gustavo Ferreira. 
# https://gist.github.com/gferreira/10da8431c22a205d4ca1


#1 se define la clase
class Square(object):
    
    fillColor = 1, 0, 0
    
    def __init__(self, side):
        self.side = side
    
    def draw(self, pos):
        x, y = pos
        fill(*self.fillColor)
        #rect(x, y, self.side, self.side)
        rect(x, y, 30, 30)


 
#2 se accede a los métodos de cada cuadrado        
S = Square(100)

S.fillColor = 0, 1, 0
S.draw((100, 300))


for i in range(0, 20):
    for j in range(0, 20):
        S.fillColor = .1+i/20, i/10, 0
        S.draw((i*40, j*40))
         