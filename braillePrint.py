def printBraille(text):
	print("Text received: " + text + '\n')
	for letter in text:
		print ("Printing character " + letter + '\n')
		#Call PyCNC script on corresponding character file
		if (letter != "\ " or letter != "\n"):
			command = "./pycnc " + "char_" + letter + ".gcode"
		elif (letter == 
	
