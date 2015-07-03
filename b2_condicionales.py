# B2- Tomar decisiones: Condicionales, if, else, if else
# if pregunta por una condición
# si es verdadero, pasa algo


# Ejemplo if
luz = "on"
if (luz == "on"):
    print "La luz esta encendida"




# if & else
a = 10 # variable
b = 20 # variable

if (a < b): 
    print "a es menor" 
else: # si es falso, sucede esto
    print "b es mayor"
    
    
    
# if, else if, else
# juan tiene hambre y plata?

si = True
no = False

plata = no
hambre = si 

if (plata == si) & (hambre == si): # si es verdadero, pasa lo siguiente   
    print "Juan se come churrasco" 
elif ( (plata == no) & (hambre == si) ):
    print "Juan pide plata a su mama"
else:
    print "Juan se queda con hambre"
    

    
