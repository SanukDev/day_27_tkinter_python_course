from tkinter import *

# Window
window = Tk()
window.title("My first window")
window.minsize(width=500, height=400)
# Add a padding
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# Using parameters common of the method

# layout managers
# my_label.pack()
# my_label.place(x=100, y=100)
my_label.grid(column=1, row=1)
# Using the dictionary
my_label["text"] = "New text"
# Using the method config
my_label.config(text="other new text")


# Button
def button_click():
    new_text = input2.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_click)
# layout managers
# button.pack()
# button.place(x=100, y=100)
button.grid(column=2, row=2)

# Entry
input2 = Entry()
# layout managers
# input2.pack()
# input2.place(x=100, y=100)
input2.grid(column=4, row=4)

# New Button
new_button = Button()
new_button.config(text="New button here")
new_button.grid(column=3, row=1)

window.mainloop()
