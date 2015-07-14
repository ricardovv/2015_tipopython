#D3- Scripts en Gyphs
#de la web de Glyphs


#- - - - - - - - - - - - 
#Seleccionar layers
myLayers = Glyphs.font.selectedLayers
for thisLayer in myLayers:
  print thisLayer.parent.name
  print thisLayer.paths
  


  
#- - - - - - - - - - - - 
#Mover nodos aleatoriamemnte
import random
random.seed()

myLayers = Glyphs.font.selectedLayers
for thisLayer in myLayers:
  for thisPath in thisLayer.paths:
    for thisNode in thisPath.nodes:
      thisNode.x += random.randint( -50, 50 )  
      
 



      
#- - - - - - - - - - - - 
# de mekkablue: https://github.com/mekkablue/Glyphs-Scripts/blob/master/Paths/Fill%20Up%20with%20Rectangles.py
     
#MenuTitle: Fill Up with Rectangles
# -*- coding: utf-8 -*-
__doc__="""
Inserts Rectangles in all empty, selected glyphs.
"""

import GlyphsApp

Font = Glyphs.font
FontMaster = Font.selectedFontMaster
selectedLayers = Font.selectedLayers

def drawRect( myBottomLeft, myTopRight ):
	try:
		myRect = GSPath()
		myCoordinates = [
			[ myBottomLeft[0], myBottomLeft[1] ],
			[ myTopRight[0], myBottomLeft[1] ],
			[ myTopRight[0], myTopRight[1] ],
			[ myBottomLeft[0], myTopRight[1] ]
		]

		for thisPoint in myCoordinates:
			newNode = GSNode()
			newNode.type = GSLINE
			newNode.position = ( thisPoint[0], thisPoint[1] )
			myRect.nodes.append( newNode )

		myRect.closed = True
		return myRect

	except Exception as e:
		return False

def process( thisLayer ):
	layerIsEmpty = ( len(thisLayer.paths) == 0 and len(thisLayer.components) == 0 )
	if layerIsEmpty:
		bottomLeft = ( 50.0, 0.0 )
		topRight = ( thisLayer.width - 50.0, 600.0 )
		layerRect = drawRect( bottomLeft, topRight )
		if layerRect:
			thisLayer.paths.append( layerRect )
			return "OK"
		else:
			return "error"
	else:
		return "not empty, skipped"

Font.disableUpdateInterface()

for thisLayer in selectedLayers:
	thisGlyph = thisLayer.parent
	thisGlyph.beginUndo()
	print "Filling %s: %s." % ( thisGlyph.name, process( thisLayer ) )
	thisGlyph.endUndo()

Font.enableUpdateInterface()






#- - - - - - - - - - - - 
#mekkablue https://github.com/mekkablue/Glyphs-Scripts/blob/master/Effects/Beowulferize.py

#MenuTitle: Beowulferize
# -*- coding: utf-8 -*-
__doc__="""
Turns selected glyphs into a pseudorandom Beowulf-lookalike.
"""

# Please adjust to your own needs:

alphabets = 5    # how many variants of each glyph will be created
shatter = 12     # how far each single node may be moved each time
reiterations = 2 # how often a node may be moved
linelength = 70  # maximum number of letters in a line for which the feature works

import GlyphsApp
import random
random.seed()

Font = Glyphs.font
selectedGlyphs = [ l.parent for l in Font.selectedLayers ]
listOfNames = [ thisGlyph.name for thisGlyph in selectedGlyphs ]
glyphsToProcess = []

def updated_code( oldcode, beginsig, endsig, newcode ):
	"""Replaces text in oldcode with newcode, but only between beginsig and endsig."""
	begin_offset = oldcode.find( beginsig )
	end_offset   = oldcode.find( endsig ) + len( endsig )
	newcode = oldcode[:begin_offset] + beginsig + newcode + "\n" + endsig + oldcode[end_offset:]
	return newcode

def create_otfeature( featurename = "calt",
                      featurecode = "# empty feature code",
                      targetfont  = Font,
                      codesig     = "DEFAULT-CODE-SIGNATURE" ):
	"""
	Creates or updates an OpenType feature in the font.
	Returns a status message in form of a string.
	"""
	
	beginSig = "# BEGIN " + codesig + "\n"
	endSig   = "# END "   + codesig + "\n"
	
	if featurename in [ f.name for f in targetfont.features ]:
		# feature already exists:
		targetfeature = targetfont.features[ featurename ]
		
		if beginSig in targetfeature.code:
			# replace old code with new code:
			targetfeature.code = updated_code( targetfeature.code, beginSig, endSig, featurecode )
		else:
			# append new code:
			targetfeature.code += "\n" + beginSig + featurecode + "\n" + endSig
			
		return "Updated existing OT feature '%s'." % featurename
	else:
		# create feature with new code:
		newFeature = GSFeature()
		newFeature.name = featurename
		newFeature.code = beginSig + featurecode + "\n" + endSig
		targetfont.features.append( newFeature )
		return "Created new OT feature '%s'." % featurename

def create_otclass( classname   = "@default",
                    classglyphs = [ x.parent.name for x in Font.selectedLayers ],
                    targetfont  = Font ):
	"""
	Creates an OpenType class in the font.
	Default: class @default with currently selected glyphs in the current font.
	Returns a status message in form of a string.
	"""
	
	# strip '@' from beginning:
	if classname[0] == "@":
		classname = classname[1:]
	
	classCode = " ".join( classglyphs )
	
	if classname in [ c.name for c in targetfont.classes ]:
		targetfont.classes[classname].code = classCode
		return "Updated existing OT class '%s'." % classname
	else:
		newClass = GSClass()
		newClass.name = classname
		newClass.code = classCode
		targetfont.classes.append( newClass )
		return "Created new OT class: '%s'." % classname

def randomize( min, max ):
	return random.randint( min, max )

def beowulferize( thisGlyph ):
	thisGlyph.beginUndo()
	for thisLayer in thisGlyph.layers:
		for thisPath in thisLayer.paths:
			for thisNode in thisPath.nodes:
				thisNode.x +=  randomize( -shatter, shatter )
				thisNode.y +=  randomize( -shatter, shatter )
				
			thisPath.checkConnections()

	thisGlyph.endUndo()



Glyphs.clearLog()
Glyphs.showMacroWindow()
print "Beowulferizing %s:" % str( Font.familyName )

Font.disableUpdateInterface()

# Create Glyph Variants:
print "Creating alternative glyphs for:",
for thisGlyph in selectedGlyphs:
	glyphsToProcess.append( thisGlyph )
	print thisGlyph.name,
	
	for round in range( alphabets ):
		newName = thisGlyph.name+".calt"+str(round)
		targetGlyph = thisGlyph.copy()
		targetGlyph.name = newName
		glyphsToProcess.append( targetGlyph )
		Font.glyphs.append( targetGlyph )

print "\nDeforming glyphs",
for thisGlyph in glyphsToProcess:
	print ".",
	for iteration in range( reiterations ):
		beowulferize( thisGlyph )

print

# Create Classes:
print create_otclass( classname="default", classglyphs=listOfNames, targetfont=Font )
for i in range( alphabets ):
	print create_otclass( classname="calt"+str(i), classglyphs=[ n+".calt"+str(i) for n in listOfNames ], targetfont=Font )

# Create OT Feature:
beowulfCode = ""
for i in range( ( alphabets * ( linelength//alphabets ) + 1 ), 0, -1 ):
	beowulfCode += "sub @default' " + "@default " * i + "by @calt" + str( ( range(alphabets) * ((linelength//alphabets)+2))[i] ) + ";\n"

print create_otfeature( featurename="calt", featurecode=beowulfCode, targetfont=Font, codesig="BEOWULFERIZER")

Font.enableUpdateInterface()








