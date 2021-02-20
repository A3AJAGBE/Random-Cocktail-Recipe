from tkinter import *

interface = Tk()
interface.title("A3AJAGBE RANDOM COCKTAIL RECIPE")
interface.config(padx=30, pady=30)

# Layout
instruction = Label(text="Instruction: ", fg="#f05454")
instruction.grid(row=0, column=0, columnspan=2)

name_label = Label(text="Name: ")
name_label.grid(row=1, column=0)
name = Entry()
name.grid(row=1, column=1)

glass_label = Label(text="Proper Glass: ")
glass_label.grid(row=2, column=0)
glass = Entry()
glass.grid(row=2, column=1)

status_label = Label(text="Cocktail Status: ")
status_label.grid(row=3, column=0)
status = Entry()
status.grid(row=3, column=1)

ingredients_label = Label(text="A list of ingredients")
ingredients_label.grid(row=4, column=0, columnspan=2, pady=10)
ingredients = Listbox()
ingredients.insert(1, "1. Bread")
ingredients.insert(2, "2. Milk")
ingredients.insert(3, "3. Meat")
ingredients.grid(row=5, column=0, columnspan=2)

# Keep the screen open until exited
interface.mainloop()