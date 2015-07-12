

"""
# create a bezier path
fill(.8, .7, .2)
path = BezierPath()

# move to a point
path.moveTo((100, 10))
# line to a point
path.lineTo((100, 150))

path.lineTo((350, 200))
# close the path
path.closePath()
# set the path as a clipping path
clipPath(path)
# the oval will be clipped inside the path

oval(100, 100, 100, 100)
"""  

translate(400, 400)
fill(.15, .15, .2)
rect(0, 0, 400, 400)

fill(.8, .2, .2)
 
# create a new empty path
newPath()
# set the first oncurve point
moveTo((0, 0))
# line to from the previous point to a new point
#lineTo((0, 0))
#lineTo((0, 0))

x1 =    50
y1 =    100

x2 =    100
y2 =    0

# curve to a point with two given handles
#arcTo((200, 100), (150, 100),  100)
arcTo((x1, y1), (x2, y2),  55)

# close the path
closePath()
# draw the path
drawPath() 