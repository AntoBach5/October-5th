from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Codingal's Text Editor")
window.geometry("800x600")

window.rowconfigure(0, minsize=800, weight=1) #First number is the index number. 
#Min size is the minimum height of the row in pixels.
#Min size sets the minimum width of the column in pixels.

#Wieght is how much extra space the row receives when the window is resized.
#We can also add "pad", that gives extra space between the rows.
window.columnconfigure(1, minsize=800, weight=1) 

def open_file():
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    if not file_path:
        return
    
    text_edit.delete(1.0, END)
    
    with open(file_path, "r") as input_file:
        text = input_file.read()
        text_edit.insert(END, text)
        
        input_file.close()

    window.title(f"Codingal's Text Editor - {file_path}")

def save_file():
    file_path = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    if not file_path:
        return
    
    with open(file_path, "w") as output_file:
        text = text_edit.get(1.0, END)
        output_file.write(text)
    
    window.title(f"Codingal's Text Editor - {file_path}")
    

text_edit = Text(window)

frame_buttons = Frame(window, relief=RAISED, bd=5) #bd is the volume that the frame has.
open_button = Button(frame_buttons, text="Open", command=open_file)

save_button = Button(frame_buttons, text="Save As...", command=save_file)

open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
save_button.grid(row=1, column=0, sticky="ew", padx=5)

frame_buttons.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()