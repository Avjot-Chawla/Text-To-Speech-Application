# Importing libraries
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
from tkinter import messagebox
import pyttsx3
import os

# Initializing the text to speech variable
engine = pyttsx3.init()

# Defining Functions
def type_text():
    tb.delete("1.0", "end")
    tb.insert("1.0", "Enter the text")

def input_file():
    tb.delete("1.0", "end")
    tb.insert("1.0", "Enter file name")

# New feature: Browse File
def browse_file():
    filename = filedialog.askopenfilename(title="Select a text file", 
                                          filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if filename:
        tb.delete("1.0", "end")
        tb.insert("1.0", filename)

def speak_now():
    # Storing speech properties 
    text = tb.get("1.0", "end").replace('\n', '')
    gender = gender_combo.get()
    speed = speed_combo.get()
    voices = engine.getProperty('voices')
    radio_value = var.get()
    
    # Checking for a valid file name if using file input
    try:
        if radio_value == 1:
            with open(text, "r") as readfile:
                text = readfile.read()
    except OSError:
        messagebox.showerror("Error", "Invalid file name")
        return

    # Set voice and run command
    def set_voice():
        if gender == "Male":
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    # Set rate and call set_voice() function
    if text:
        if speed == "Fast":
            engine.setProperty('rate', 300)
        elif speed == "Normal":
            engine.setProperty('rate', 150)
        else:
            engine.setProperty('rate', 60)
        set_voice()

def download():
    # Storing speech properties 
    text = tb.get("1.0", "end")
    gender = gender_combo.get()
    speed = speed_combo.get()
    voices = engine.getProperty('voices')
    radio_value = var.get()
    
    # Checking for a valid file name if using file input
    try:
        if radio_value == 1:
            with open(text, "r") as readfile:
                text = readfile.read()
    except OSError:
        messagebox.showerror("Error", "Invalid file name")
        return

    # Set voice and run command
    def set_voice():
        try:
            path = filedialog.askdirectory(title="Select Directory to Save")
            if not path:
                return
            os.chdir(path)
            if gender == "Male":
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            engine.save_to_file(text, 'text_to_speech.mp3')
            engine.runAndWait()
        except OSError:
            return

    # Set rate and call set_voice() function
    if text:
        if speed == "Fast":
            engine.setProperty('rate', 300)
        elif speed == "Normal":
            engine.setProperty('rate', 160)
        else:
            engine.setProperty('rate', 60)
        set_voice()

# Creating colour variables
bl = "#008FFF"
bk = "#000000"
w = "#FFFFFF"

# Creating tkinter GUI window
root = Tk()
root.title("Text to Speech")
root.geometry("900x450+300+180")
root.resizable(False, False)
root.config(bg=bk)

# Input the icon image
icon_image = PhotoImage(file="speak.png")
root.iconphoto(False, icon_image)

# Creating a Frame
top_frame = Frame(root, bg=w, width=900, height=100)
top_frame.place(x=0, y=0)

# Input speaker logo image
Logo = PhotoImage(file="speaker_logo.png")
Label(top_frame, image=Logo, bg=w).place(x=10, y=5)

# Creating text box 
tb = Text(root, font="Robote 15", borderwidth=5)
tb.place(x=10, y=150, width=500, height=270)
tb.insert("1.0", "Enter the text")

# Creating Radio Buttons
var = IntVar()
r1 = Radiobutton(root, text="Type Text", variable=var, value=0, command=type_text)
r1.place(x=590, y=160)
r2 = Radiobutton(root, text="Input File", variable=var, value=1, command=input_file)
r2.place(x=760, y=160)

# Browse Button for File Input
browse_btn = Button(root, text="Browse", width=10, font="12", bg=bk, fg=w, command=browse_file)
browse_btn.place(x=740, y=195)

# Creating Labels
Label(root, text="VOICE", font="20", bg=bk, fg=w).place(x=595, y=240)
Label(root, text="SPEED", font="20", bg=bk, fg=w).place(x=760, y=240)
Label(top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg=w, fg=bk).place(x=100, y=40)

# Creating Comboboxes
gender_combo = Combobox(root, values=["Male", "Female"], font="12", width=10, state='r')
gender_combo.place(x=560, y=280)
gender_combo.set("Male")

speed_combo = Combobox(root, values=["Fast", "Normal", "Slow"], font="12", width=10, state='r')
speed_combo.place(x=730, y=280)
speed_combo.set("Normal")

# Creating image icons for buttons
img_icon1 = PhotoImage(file="speak.png")
img_icon2 = PhotoImage(file="download.png")

# Creating Buttons
b1 = Button(root, text="Speak", compound=LEFT, image=img_icon1, width=150, font="12", bg=bk, fg=w, bd=5, command=speak_now)
b1.place(x=540, y=340)

b2 = Button(root, text="Save", compound=LEFT, image=img_icon2, width=150, font="12", bg=bk, fg=w, bd=5, command=download)
b2.place(x=710, y=340)

root.mainloop()
