import makeScript as script
import os
def printBraille(text):
        print("Text received: " + text + '\n')
        filesToConcatenate = ["gcode/start.gcode"]
        i = 0
        #j = 0
        for letter in text:
            i += 1
            #Check if we need to go to a newline
            if (i % 17 == 0):
                filesToConcatenate.append("gcode/newline.gcode")
                #j += 1
                i = 0
            #Check if we need to adjust for y position (every 8)
            #if (j % 8 == 0 and j != 0):
                #filesToConcatenate.append("gcode/readjusty.gcode")
            #if (i % 10 == 0):
                #filesToConcatenate.append("gcode/readjustx.gcode")
            print("Printing character " + letter + '\n')
            #Call PyCNC script on corresponding character file
            if (letter.isupper()):
                filesToConcatenate.append("gcode/uppercase.gcode")
                filesToConcatenate.append("gcode/space.gcode")
                i += 1
            if ((not letter.isalpha()) and (not letter.isdigit()) and (letter not in ["?",".",",","!"," ","\n","\t",":",";","-","'"])):
                    print("Character not printable!")
            elif (letter.lower() in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","!","#","?",":",";"]):
                filesToConcatenate.append("gcode/char_"+letter+".gcode")
                filesToConcatenate.append("gcode/space.gcode")
            elif (letter == " "):
                filesToConcatenate.append("gcode/space.gcode")
            elif (letter == "."):
                filesToConcatenate.append("gcode/char_period.gcode")
                filesToConcatenate.append("gcode/space.gcode")
            elif (letter == ","):
                filesToConcatenate.append("gcode/char_comma.gcode")
                filesToConcatenate.append("gcode/space.gcode")
            elif (letter == "?"):
                filesToConcatenate.append("gcode/char_questions.gcode")
                filesToConcatenate.append("gcode/space.gcode")
            elif (letter == "-"):
                filesToConcatenate.append("gcode/char_hyphen.gcode")
                filesToConcatenate.append("gcode/space.gcode")
            elif (letter == "'"):
                filesToConcatenate.append("gcode/char_apostraphe.gcode")
                filesToConcatenate.append("gcode/space.gcode")
            elif (letter == "\t"):
                for k in range(4):
                    filesToConcatenate.append("gcode/space.gcode")
                    i += 1
                    if (i % 31 == 0):
                        filesToConcatenate.append("gcode/newline.gcode")
                        #j += 1
                        i = 0
                        #Check if we need to adjust for y position (every 8)
                    #if (j % 8 == 0):
                        #filesToConcatenate.append("gcode/readjusty.gcode")
                    #if (i % 10 == 0):
                        #filesToConcatenate.append("gcode/readjustx.gcode")
            elif (letter == "\n"):
                #j += 1
                i = 0
                filesToConcatenate.append("gcode/newline.gcode")
        filesToConcatenate.append("gcode/end.gcode")
        flag = script.makeScript(filesToConcatenate)
        if flag:
            command = "sudo ../../PyCNC/pycnc "+ "script.gcode"
            os.system(command)
            print("Finished Printing. Waiting on new command...\n")
        else:
             print("Error generating script.")
        return

