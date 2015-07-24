#D2- Scripts en Gyphs
# ejemplos tomados desde la web de Glyphs
# solo para uso educacional



#mostrando los objetos 
print Glyphs.fonts # fuente abierta
print Glyphs.currentDocument # fuente actual
print Glyphs.font.glyphs #objeto glyph
print Glyphs.font.glyphs[7] #objeto glyph por su posición en la lista


#por propiedades
print Glyphs.font.glyphs["a"].name
print Glyphs.font.glyphs["a"].category
print Glyphs.font.glyphs["a"].subCategory
print Glyphs.font.glyphs["a"].unicode


#usando variables
myG = "a"
print Glyphs.font.glyphs[myG].name
print Glyphs.font.glyphs[myG].category
print Glyphs.font.glyphs[myG].subCategory
print Glyphs.font.glyphs[myG].unicode


#usando ciclo for
#para cada g en la lista de objetos Glyphs.font.glyphs
for g in Glyphs.font.glyphs:
  print g.name, g.category, g.subCategory, g.unicode

