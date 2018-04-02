import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import speech2text as s2t
import pdf2text as p2t 
import braillePrint as printer
import keyboardInput as keyboard
# Uncomment line below and comment first line to run in python 2.X
#import Tkinter as tk

def write_pdf_to_text():
	print("PDF to Text Chosen")
	#filepath = "C:/Users/Ryan Schreiber/Desktop/School/CSCE 483/pytesseract demo/test1.JPG"
	filename = filedialog.askopenfilename(filetypes = (("JPG files", ("*.jpg","*.jpeg"))
                                                         ,("PNG files", "*.png")
                                                         ,("PDF files", "*.pdf") ))
	text = p2t.pdfToText(filename)
	printer.printBraille(text)
	
def write_speech_to_text():
	print("Speech to Text Chosen")
	text = s2t.speechToText()
	printer.printBraille(text)

def write_keyboard_text():
	print("Keyboard Input Chosen")
	text = make_keyboard_input_window()
	printer.printBraille(text)

def make_keyboard_input_window():
	window = tk.Toplevel(root)
	textEntry = tk.Entry(window)
	textEntry.pack()
	waitVar = tk.IntVar()
	submitButton = tk.Button(window, text = "Submit", command = lambda: waitVar.set(1))
	submitButton.pack()
	# Test print
	print("waiting on text input...")
	submitButton.wait_variable(waitVar)
	print("done waiting")
	text = textEntry.get()
	window.destroy()
	return text

root = tk.Tk()
root.title("Brailler")
root.attributes("-fullscreen", True)
frame = tk.Frame(root)
frame.pack_propagate(0)
frame.pack(fill = tk.BOTH, expand = 1)

welcomeLabel = tk.Label(frame, justify = tk.CENTER, text = "Welcome to Brailler")
welcomeLabel.config(font = ("System", 36))
welcomeLabel.pack(side = tk.TOP)

# PDF to Text Button
pdfButton = tk.Button(frame, text = "PDF-to-Text", font = ("System", 20), command = write_pdf_to_text)
pdfButton.pack(side = tk.LEFT)
# End PDF to Text Button

# Speech to Text Button
speechButton = tk.Button(frame, text = "Speech-to-Text", font = ("System", 20), command = write_speech_to_text)
speechButton.pack(side = tk.LEFT)
# End Speech to Text Button

# Keyboard Input Button
keyboardButton = tk.Button(frame, text = "Keyboard Input", font = ("System", 20), command = write_keyboard_text)
keyboardButton.pack(side = tk.LEFT)
# End Keyboard Input Button

# Quit Button
quitButton = tk.Button(frame, text = "Quit", font = ("System", 20), fg = "red", command = quit)
quitButton.pack(side = tk.LEFT)
# End Quit Button


root.mainloop()
