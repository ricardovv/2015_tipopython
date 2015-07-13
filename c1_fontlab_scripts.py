#C1- Scripts para Fontlab
# referencias fontlab clases y metodos
#http://www.e-font.de/flpydoc/html/FontLab.xml.html
# abrir fontlab, 
# abrir una fuente de prueba (por ejemplo EBGaramond-0.016)
# abrir panel para scripts: View/Tolbars/Macro

# estas lineas "importa" un  modulo propio de FontLab (existe solo en Fontlab)
#from FL import * 

# fl.font objeto. fuente actual
# glyphs. una propiedad de font
# se accede con notacion de puntos


from FL import * 

# C1.a - nombre y unicode 
#print fl.font #Nombre de la fuente actual
#print fl.glyph #Glyph activo y los nodps que tiene 
#print fl.path # la ruta de donce esta fontlab
#print fl.count_selected # glyphs seleciconados 
#print fl.EditGlyph(20) # abre glyph segun index dado, int

#print fl.font["b"].name #seleeciona un glyph y muestra su nombre
#print fl.font["b"].unicode
#print fl.font.x_height[9] 
#print fl.font.ascender[9]

#Miembros de la classe Font 
#print fl.font.features #list of opentype features  
#print fl.font.classes #list of classes
#print fl.font.glyphs #list of classes

#print fl.font.glyphs[12].width # ver el ancho de un glyph dado


#####
print fl.font.features[2] #list of opentype features


# C1.a - Lista de los gliphs en una fuente 
for l in fl.font.glyphs:
	print l.name
	
	
# lo mismo pero c variables	
"""
mifuente = fl.font
misletras = mifuente.glyphs

for l in misletras:
	print l.name
"""

# Com recorrerlos todos usando ciclo for 
for g in fl.font.glyphs:
	print  "nombre: ",g.name, "ancho:r ",  g.width
	# ver el ancho de un glyph dado
	
	
