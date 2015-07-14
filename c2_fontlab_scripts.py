#C1- Scripts para Fontlab
# referencias fontlab clases y metodos
# http://www.e-font.de/flpydoc/ 
# font lista de glyphs, glyphs lista de nodos y otros objetos
# getters y setters, leer o signar un valor. 

# Crear, nombrar y guardar programas porpios
#FLM: Nombre del Programa



# - - - - - - - - - - - 
# muestra nombre de glyph
from FL import *

"""		 
#1
for g in fl.font.glyphs:
	#chi, f_, .sc, .cap, circumflex
	#inferior, bullet, acute, oldstyle, comma, ord, _
	if "f_" in g.name:
		print g.name
		print "-------" 
"""

"""
#2 usando variables
f = fl.font.glyphs
count = 0 

for g in f:
	#chi, f_, .sc, .cap, circumflex
	#inferior, bullet, acute, oldstyle, comma, ord, _
	if "f_" in g.name:
		count+=1
		print count, "- ", g.name
		print "-------" 
"""         



# - - - - - - - - - - - 
# encuentra un valor en el nombre del glyph y lo destaca    
from FL import *

"""
#imprime el nombre de todos los glyphs
#como se podran numerar?
gs = fl.font.glyphs
for g in gs:
		print "- - -r ", g.name
"""


"""
#busca glyphs c ciertas palabas en su nombre
#las masrca y las imprime
for g in gs:
	#chi, f_, .sc, .cap, circumflex
	#inferior, bullet, acute, oldstyle, comma, ord, _
	if "f_" in g.name:
		g.mark = 222
		print g.nodes_number, "-", g.name
		print "- - - - - - - -"
	else:
		g.mark = 20
fl.UpdateFont(fl.ifont)
"""
 

"""
# - - - - - - - - - - - 
# Ejemplo de FontLab Studio manual PDF 
# Encontrar glyphs vacios (sin outline o componentes), como “espacio” 
from FL import * 
num = 0 #contador parte en cero 
for g in fl.font.glyphs:
    if len(g) == 0 and len(g.components) == 0:
        print num, "- ", g.name 
        num+=1 # se le agrega uno a lo que vale		
        print "-------"
"""

       

