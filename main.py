from tkinter import *
import requests
import io
from urllib.request import urlopen
# installed pillow
from PIL import Image, ImageTk

COCKTAIL_ENDPOINT = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
response = requests.get(COCKTAIL_ENDPOINT)
response.raise_for_status()
data = response.json()['drinks']

# Get the list of ingredients
ingredients_list = []
for num in range(1, 16):
    item = f"strIngredient{num}"
    cocktail_ingredient = data[0][item]
    if cocktail_ingredient is not None:
        add = f"{num}. {cocktail_ingredient}"
        ingredients_list.append(add)

# Get ingredients measurements
measurement_list = []
for num in range(1, 16):
    measure = f"strMeasure{num}"
    cocktail_measurement = data[0][measure]
    if cocktail_measurement is not None:
        measurement_list.append(cocktail_measurement)

# combine the two lists
new_dict = {k: v for k, v in zip(ingredients_list, measurement_list)}

# UI setup
interface = Tk()
interface.title("A3AJAGBE RANDOM COCKTAIL RECIPE")
interface.config(padx=30, pady=30)

# Layout
cocktail_image = data[0]['strDrinkThumb']
canvas = Canvas(width=200, height=200)
image_url = f"{cocktail_image}/preview"

# Read the image from the url
image = urlopen(image_url)
# create an image file object
image = io.BytesIO(image.read())
# use PIL to open image formats like .jpg  .png  .gif  etc.
image = Image.open(image)
# convert to an image Tkinter can use
cocktail_picture = ImageTk.PhotoImage(image)

canvas.create_image(100, 100, image=cocktail_picture)
canvas.grid(row=0, column=0, columnspan=2)

cocktail_name = data[0]["strDrink"]
name_label = Label(text="Name: ")
name_label.grid(row=1, column=0)
name = Entry()
name.insert(END, cocktail_name)
name.grid(row=1, column=1)

cocktail_glass = data[0]["strGlass"]
glass_label = Label(text="Glass: ")
glass_label.grid(row=2, column=0)
glass = Entry()
glass.insert(END, cocktail_glass)
glass.grid(row=2, column=1)

cocktail_status = data[0]["strAlcoholic"]
status_label = Label(text="Cocktail Status: ")
status_label.grid(row=3, column=0)
status = Entry()
status.insert(END, cocktail_status)
status.grid(row=3, column=1)

cocktail_instruction = data[0]['strInstructions']
canvas = Canvas(width=300, height=150, bg="#0066ff")
canvas.create_text(150, 75, text=cocktail_instruction, width=250, font=("italic",), fill="white")
canvas.grid(row=4, column=0, columnspan=2)

ingredients = Listbox(width=40)
ingredients.insert(1, "The Cocktail Recipe: ")
num = 1
for data in new_dict:
    num += 1
    m = new_dict[data]
    result = f"{data} / {m}"
    ingredients.insert(num, result)
ingredients.grid(row=5, column=0, columnspan=2, pady=20)

# Keep the screen open until exited
interface.mainloop()
