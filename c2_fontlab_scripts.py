#C1- Scripts para Fontlab
# referencias fontlab clases y metodos
# http://www.e-font.de/flpydoc/ 

from FL import * 

# Crear, nombrar y guardar programas porpios
#FLM: Nombre del Programa



# - - - - - - - - - - - 
# Ejemplo de FontLab Studio manual PDF 
# Encontrar glyphs vacios (sin outline o componentes), como “espacio” 
num = 0 #contador parte en cero 
for g in fl.font.glyphs:
    if len(g) == 0 and len(g.components) == 0:
        print num, "- ", g.name 
        num+=1 # se le agrega uno a lo que vale		
        print "-------"
       

# - - - - - - - - - - - 
for g in fl.glyphs:
    if ".onum" in g.name
        print g.name
        print "-------" 
        
for g in fl.font.glyphs:
	if ".onum" in g.name:
		print g.name        