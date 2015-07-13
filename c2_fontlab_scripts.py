#C1- Scripts para Fontlab
# referencias fontlab clases y metodos
# http://www.e-font.de/flpydoc/ 


from FL import * 





# Crear, nombrar y guardar programas porpios
#FLM: Nombre del Programa


# - - - - - - - - - - - 
# Ejemplo de FontLab Studio manual PDF 
#Suppose we want to find all the glyphs that are empty: 
#i.e. don’t have an outline or any components. 
#The “space” is a good example of such a glyph.

for g in fl.font.glyphs:
	if len(g) == 0 and len(g.components) == 0:
		print g.name
		

# - - - - - - - - - - - 
print "-------"
#print fl.iglyph # Index of the currently active glyph in the current font
print fl.count_selected # cuent uantos glyphs estan seleccionados
		