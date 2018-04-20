def printBraille(text):
        print("Text received: " + text + '\n')
        filesToConcatenate = []
        for letter in text:
            print("Printing character " + letter + '\n')
            #Call PyCNC script on corresponding character file
            if ((not letter.isalpha()) and (not letter.isdigit()) and (letter not in ["?",".",",","#","!"," ","\n","\t",":",";"])):
                    print("Character not printable!")
                    return
            elif (letter in ["a","b","c","d","e","f","g","h","i","j","k","l","m","o","p","q","r","s","t","u","v","w","x","y","z"]):
	            filesToConcatenate.append("gcode/char_"+letter+".gcode")
            elif (letter == " "):
	    	    command = "./pycnc space.gcode" 
	    elif (letter == "\n"):
	    	    command = "./pycnc newline.gcode"
	    print("Executing command: " + command + "\n")
        
        filesToConcatenate.append("end.gcode")
        makeScript(filesToConcatenate)
        command = "sudo ../PyCNC/pycnc "+ "../Brailler/gcode/script.gcode"
	print("Finished Printing. Waiting on new command...\n")
	return
