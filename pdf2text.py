


## -------------------------------------------------------------------------- ##
## import needed libraries

from os import system,listdir,getcwd,remove
import sys

sys.path.append("C:\Program Files (x86)\Tesseract-OCR")

# boolean to whether to continue with running the program
everythingIsWorking = True

# use in cmd "pip install PIL"
try:
    from PIL import Image
except:
    print ("Needed library not installed: PIL")

# use in cmd "pip install pytesseract"
# use in cmd "pip install pytesseract_OCR"
try:
    import pytesseract
except:
    print ("Needed library not installed: pytesseract")
    print ("Needed library not installed: pytesseract_OCR")

# determine whether to continue
if not everythingIsWorking:
    input("Program will terminate because you are missing dependent libraries.")
    quit()





## -------------------------------------------------------------------------- ##
## The main function that we will be using to convert images to strings.
def pdfToText(filepath):
    imageObject = None
    if filepath.split(".")[-1] == "pdf":
        tempPath     = convertPDFtoJPG(filepath)
        stringOutput = ""

        for file in listdir(tempPath):
            print(tempPath+file)
            imageObject  = Image.open(tempPath+file)
            stringOutput += pytesseract.image_to_string(imageObject)
            imageObject.close()
            remove(tempPath+file)
        
        return stringOutput
    imageObject = Image.open(filepath)
    output = pytesseract.image_to_string(imageObject)
    return (output)

def convertPDFtoJPG(filepath):
    dst = '"'+getcwd().replace("\\","/")+"/tmp/"+'"'
    system("2jpeg -src "+filepath+" -dst "+dst)
    return dst.replace('"',"")










