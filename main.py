from tkinter import *
from tkinter import messagebox
import pyautogui as pag

def help_func():
    messagebox.showinfo("Help" , "f - Find position \nc - Ccopy position\ne -Exit" )

# Define the function to display the mouse position
def show_mouse_position(event):
    def put_data_in_entries(x,y):
        x_entry.config(state=NORMAL)
        y_entry.config(state=NORMAL)
        x_entry.delete(0,END)
        y_entry.delete(0,END)
        x_entry.insert(0,x)
        y_entry.insert(0,y)
        x_entry.config(state="readonly")
        y_entry.config(state="readonly")
    x,y = pag.position()
    put_data_in_entries(x,y)

# Define the function to copy the mouse position to the clipboard
def copy_mouse_position(event):
    # Get the mouse position
    x,y = pag.position()
    # Copy the mouse position to the clipboard
    window.clipboard_clear()
    window.clipboard_append(f"({x}, {y})")
# Define the function to exit the program
def exit_program(*args):
    # Exit the program
    window.destroy()

# Create the main window
window = Tk()
window.minsize(200,220)
window.maxsize(200,220)



font = ("Axial" ,15)
# X Co-ordinate:
Label(window, text="X Co-ordinate:" , font=font ).place(x=5 , y=10 )
x_entry = Entry(font=font , state="readonly")
x_entry.place(x=10 , y=40  , height=30 , width=150 )
# Y Co-ordinate:
Label(window, text="Y Co-ordinate:" , font=font ).place(x=5 , y=80 )
y_entry = Entry(font=font , state="readonly")
y_entry.place(x=10 , y=120  , height=30 , width=150 )

# Bind the "f" key to the function that displays the mouse position
window.bind("<KeyPress-f>", show_mouse_position)
# Bind the "c" key to the function that copies the mouse position to the clipboard
window.bind("<KeyPress-c>", copy_mouse_position)
# Bind the "e" key to the function that exits the program
window.bind("<KeyPress-e>", exit_program)

menu = Menu(master=window , tearoff=False )
menu.add_command(label="Help" , command=help_func)

window.config(menu=menu)

# Start the main loop
window.mainloop()
