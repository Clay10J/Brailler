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
	text = s2t.captureAudioToText()
	printer.printBraille(text)

def write_keyboard_text():
	print("Keyboard Input Chosen")
	text = make_keyboard_input_window()
	printer.printBraille(text)

def make_keyboard_input_window():
	window = tk.Toplevel(root)
	inputText = tk.Text(window)
	inputText.pack()
	waitVar = tk.IntVar()
	submitButton = tk.Button(window, text = "Submit", command = lambda: waitVar.set(1))
	submitButton.pack()
	# Test print
	print("waiting on text input...")
	submitButton.wait_variable(waitVar)
	print("done waiting")
	text = inputText.get("1.0", "end-1c")
	window.destroy()
	return text

root = tk.Tk()
root.title("Brailler")
root.attributes("-fullscreen", True)
tk.Grid.rowconfigure(root, 0, weight = 1)
tk.Grid.columnconfigure(root, 0, weight = 1)
#root.grid_propagate(0)
frame = tk.Frame(root)
#frame.grid_propagate(0)
frame.grid(row = 0, column = 0, sticky = tk.N + tk.S + tk.E + tk.W)

# Grid Filler
for row_index in range(1, 10):
    tk.Grid.rowconfigure(frame, row_index, weight = 1)
    for col_index in range(12):
        tk.Grid.columnconfigure(frame, col_index, weight = 1)
        gridFiller = tk.Label(frame, justify = tk.CENTER, text = "")
        gridFiller.grid(row = row_index, column = col_index, sticky = tk.N + tk.S + tk.E + tk.W)  
# End Grid Filler

# Welcome Label
welcomeLabel = tk.Label(frame, justify = tk.CENTER, text = "Welcome to Brailler")
welcomeLabel.config(font = ("System", 36))
welcomeLabel.grid(row = 0, column = 0, columnspan = 12, sticky = tk.N + tk.S + tk.E + tk.W)
# End Welcome Label

# PDF to Text Button
pdfButton = tk.Button(frame, text = "PDF-to-Text", font = ("System", 20), command = write_pdf_to_text)
pdfButton.grid(row = 12, column = 0, columnspan = 3, sticky = tk.N + tk.S + tk.E + tk.W)
# End PDF to Text Button

# Speech to Text Button
speechButton = tk.Button(frame, text = "Speech-to-Text", font = ("System", 20), command = write_speech_to_text)
speechButton.grid(row = 12, column = 3, columnspan = 3, sticky = tk.N + tk.S + tk.E + tk.W)
# End Speech to Text Button

# Keyboard Input Button
keyboardButton = tk.Button(frame, text = "Keyboard Input", font = ("System", 20), command = write_keyboard_text)
keyboardButton.grid(row = 12, column = 6, columnspan = 3, sticky = tk.N + tk.S + tk.E + tk.W)
# End Keyboard Input Button

# Quit Button
quitButton = tk.Button(frame, text = "Quit", font = ("System", 20), fg = "red", command = quit)
quitButton.grid(row = 12, column = 9, columnspan = 3, sticky = tk.N + tk.S + tk.E + tk.W)
# End Quit Button


root.mainloop()
