import math


# create a bezier path
path = BezierPath()
# move to a point
path.moveTo((100, 100))
# line to a point
path.lineTo((100, 200))
path.lineTo((200, 200))
# close the path
path.closePath()
# loop over a range of 10
#drawPath(path)
    #path.lineTo((200, 200))
    # close the path
    #path.closePath()
    # loop over a range of 10
    #drawPath(path)

def arco(posx, angle):
    stroke(0)
    for a  in range(0, 200):  
        x = math.sin(a/angle)*50
        y = math.cos(a/angle)*50
        line(    (0+posx, 0), (x+posx, y)    )
        
translate(10, 800)
for cadacurva in range(1, 10):
    stroke(0, 0)
    fill(.2, .2)
    oval(50+cadacurva*100, -50, -100, 100)
    arco(cadacurva*100, cadacurva+300.)
    arco(cadacurva*100, cadacurva+300.)
    
    
translate(100, -400)
strokeWidth(1)

path = BezierPath()
# move to a point
for a  in range(0, 250):  
    angle = .01
    x = math.sin(a*angle)*50
    y = math.cos(a*angle)*50
    path.moveTo((0, 0))
    path.lineTo((x, y))
    drawPath(path)


    