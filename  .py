#C1- Scripts para Fontlab
# referencias fontlab clases y metodos
#http://www.e-font.de/flpydoc/html/FontLab.xml.html
# abrir fontlab, 
# abrir una fuente de prueba (por ejemplo EBGaramond-0.016)
# abrir panel para scripts: View/Tolbars/Macro

# estas lineas "importa" un modulo propio de FontLab (existe solo en Fontlab)
#from FL import * 

# fl.font objeto. fuente actual
# glyphs. una propiedad de font
# se accede con notacion de puntos


from FL import * 

#1 - nombre y unicode 
#print fl.font #Nombre de la fuente actual
#print fl.glyph #Glyph activo y los nodos que tiene 
#print fl.path # la ruta de donde esta fontlab
#print fl.count_selected # glyphs seleccionados 
#print fl.EditGlyph(20) # abre glyph segun index dado, int

#print fl.font["b"].name #selecciona un glyph y muestra su nombre
#print fl.font["b"].unicode
#print fl.font.x_height[9] 
#print fl.font.ascender[9]


#Miembros de la classe Font 
#print fl.font.features #list of opentype features  
#print fl.font.classes #list of classes
#print fl.font.glyphs #list of classes

#g = 200
#print fl.font.glyphs[g].name, fl.font.glyphs[100].width # ver el ancho de un glyph dado

#print fl.iglyph # Index of the currently active glyph in the current font
#print fl.count_selected # cuenta cuantos glyphs estan seleccionados de la paleta		
#print fl.font.features[2] #list of opentype features

# Fontlab reference
#print Font().__doc__"""
#2 - Lista de los gliphs en una fuente 
for l in fl.font.glyphs:
	print l.name
"""	
	
	
	
# lo mismo pero usando variables	
"""
#3
mifuente = fl.font
misletras = mifuente.glyphs

for l in misletras:
	print l.name
"""



"""
#4 Como recorrerlos todos usando ciclo for 
for g in fl.font.glyphs:
	print  "nombre: ",g.name, "ancho:r ",  g.width
	# ver el ancho de un glyph dado
"""	
	
