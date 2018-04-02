def printBraille(text):
	print("Text received: " + text + '\n')
	for letter in text:
		print ("Printing character " + letter + '\n')
		#Call PyCNC script on corresponding character file
		if ((not letter.isalpha()) and (not letter.isdigit()) and (letter not in ["?",".",",","#","!"," "])):
			print ("Character not printable!")
			return
		if ((letter != " ") or (letter != "\n")):
			command = "./pycnc " + "char_" + letter + ".gcode"
		elif (letter == " "):
			command = "./pycnc space.gcode" 
		elif (letter == "\n"):
			command = "./pycnc newline.gcode"
		print("Executing command: " + command + "\n")

	print("Finished Printing. Waiting on new command...\n")
	return
