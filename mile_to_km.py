from tkinter import *

MILES = 1.6093

# Window
window = Tk()
window.title("Calculate Mile to KM")
window.minsize(width=400, height=400)
window.config(padx=20, pady=20)

# labels
equal = Label(text="is equal to")
equal.grid(column=0, row=1)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

km = Label(text="KM")
km.grid(column=2, row=1)

result_km = Label(text=0)
result_km.grid(column=1, row=1)
# Entry
entry_miles = Entry()
entry_miles.grid(column=1, row=0)
def calculate_miles():
    miles_int = int(entry_miles.get())
    km = MILES * miles_int
    result_km.config(text=int(km))
# Button
button = Button(text="calculate", command=calculate_miles)
button.grid(column=1, row=2)



window.mainloop()
