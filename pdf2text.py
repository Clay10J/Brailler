


## -------------------------------------------------------------------------- ##
## import needed libraries

from os import system,listdir,getcwd,remove
import sys
from tika import parser

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
        return convertPDFtoText(filepath)
    imageObject = Image.open(filepath)
    output = pytesseract.image_to_string(imageObject)
    return (output)

def convertPDFtoText(filepath):
    print("converting pdf to text...")
    parsed = parser.from_file(filepath)
    content = parsed["content"]
    while "\n\n" in content:
        content = content.replace("\n\n","\n")
    return content










