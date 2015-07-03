

# para fontlab

# a.1 Lista de los gliphs en una fuente 
#importa un  modilo de FontLab, existe solo en Fontlab
from FL import * 
# fl.font objeto. fuente actual
# glyphs. una propiedad de font
# se accede con notacion de puntos

print fl.font["b"].name
print fl.font["b"].unicode

for l in fl.font.glyphs:
	print l.name
	
	
# a.2 lo mismo pero c variables	
"""
mifuente = fl.font
misletras = mifuente.glyphs

for l in misletras:
	print l.name
	"""