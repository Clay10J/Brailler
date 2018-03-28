import tkinter as tk
import speech2text as s2t
import pdf2text as p2t 
import braillePrint as printer
# Uncomment line below and comment line above to run in python 2.X
#import Tkinter as tk

def write_pdf_to_text():
	print("PDF to Text Chosen")
	text = p2t.pdfToText()
	printer.printBraille(text)
	

def write_speech_to_text():
	print("Speech to Text Chosen")
	text = s2t.speechToText()
	printer.printBraille(text)

def write_keyboard_text():
	print("Keyboard Input Chosen")

root = tk.Tk()
root.title("Brailler")
frame = tk.Frame(root)
frame.pack()

tk.Label(frame, justify=tk.CENTER, text="Welcome to Brailler").pack(side=tk.TOP)

# PDF to Text Button
pdfButton = tk.Button(frame, text="PDF-to-Text", command=write_pdf_to_text)
pdfButton.pack(side=tk.LEFT)
# End PDF to Text Button

# Speech to Text Button
speechButton = tk.Button(frame, text="Speech-to-Text", command=write_speech_to_text)
speechButton.pack(side=tk.LEFT)
# End Speech to Text Button

# Keyboard Input Button
keyboardButton = tk.Button(frame, text="Keyboard Input", command=write_keyboard_text)
keyboardButton.pack(side=tk.LEFT)
# End Keyboard Input Button

# Quit Button
quitButton = tk.Button(frame, text="Quit", fg="red", command=quit)
quitButton.pack(side=tk.LEFT)
# End Quit Button


root.mainloop()
