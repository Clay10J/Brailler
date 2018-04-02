


## -------------------------------------------------------------------------- ##
## import needed libraries

from os import system

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
    imageObject = Image.open(filepath)
    output = pytesseract.image_to_str(imageObject)
    return (output)










