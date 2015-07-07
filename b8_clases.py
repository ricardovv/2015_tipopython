# B8, CLASES
# Ejemplo basado en Gistavo Ferreira. 
#https://gist.github.com/gferreira/10da8431c22a205d4ca1


class Square(object):
    
    fillColor = 1, 0, 0
    
    def __init__(self, side):
        self.side = side
    
    def draw(self, pos):
        x, y = pos
        fill(*self.fillColor)
        rect(x, y, self.side, self.side)
        
S = Square(200)
S.draw((100, 100))
 
S.fillColor = 0, 1, 0
S.draw((100, 300))

S.fillColor = 1, 1, 0
S.draw((100, 500))