import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

current_img = None
ing_label = []

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, smooth=True, **kwargs)

def show_img(image_path):
    global current_img
    img = Image.open(image_path).resize((400, 300))
    current_img = ImageTk.PhotoImage(img)

    selected_food_img.config(image=current_img, anchor="center")


def on_box_click(title, image_path):
    global food_items

    show_img(image_path)
    selected_food_title.config(text=title,font=("Arial", 24, "bold"))

    for label in ing_label:
        label.destroy()
    ing_label.clear()

    for item in food_items:
        if title == item[1]:
            rely = 0.15
            for ing in list(item[4]):
                ingredient_label = tk.Label(root, text=ing, font=("Helvetica", 10))
                ingredient_label.place(relx = 0.35,rely = rely)
                rely += 0.05
                ing_label.append(ingredient_label)

def create_food_box(image_path, title, time, rating, index):
    img = Image.open(image_path)
    img = img.resize((150, 100))
    photo = ImageTk.PhotoImage(img)

    img_id = canvas_food.create_image(20 + index * 200, 50, anchor="nw", image=photo)
    images.append(photo)

    canvas_food.create_text(20 + index * 200 + 75, 170, text=title, font=("Arial", 12, "bold"), fill="#333", anchor="center")
    canvas_food.create_text(20 + index * 200 + 75, 210, text=time, font=("Arial", 10), fill="#777", anchor="center")
    canvas_food.create_text(20 + index * 200 + 75, 230, text=rating, font=("Arial", 10), fill="#777", anchor="center")


    canvas_food.tag_bind(img_id, '<Button-1>', lambda e: on_box_click(title,image_path))


root = tk.Tk()

root.title("My app")

# Правим прозореца на цял екран
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
root.geometry(f"{WIDTH}x{HEIGHT}")

# Фиксираме размера на прозореца (не може да се променя)
root.resizable(False, False)

#Лента с текст
purple_frame = tk.Frame(root, bg="#685cfc", width=WIDTH, height=50)
purple_frame.pack(pady = 20,fill="x")

label = tk.Label(purple_frame, text="Choose a food for today's meal", font=("Arial", 16, "bold"), fg="white", bg="#685cfc")
label.pack(pady=10)

#Mein изображение
MAIN_PICTURE = Image.open("Images/9fef138b7f92801b7dbfb3afcc023e53.webp")
MAIN_PICTURE_Tk = ImageTk.PhotoImage(MAIN_PICTURE)


main_image_label = ttk.Label(root,image=MAIN_PICTURE_Tk)
main_image_label.place(relx=0.625, rely=0.1)


#Създаване на гуудс
canvas = tk.Canvas(root, width=200, height=HEIGHT)
canvas.place(rely= 0.1,relx=0.89)

start_y = 0
spacing = 70

categories = ["Vegetarian", "Vegan", "Gluten-free", "Dairy-free","Healthy","Quick","Easy"]
for index, category in enumerate(categories):
    y1 = start_y + index * spacing
    y2 = y1 + 50

    create_rounded_rectangle(canvas, 10, y1, 150, y2, radius=25, fill="white", outline="#E8E8E8", width=2)
    canvas.create_text(25, (y1 + y2) // 2, text="✔", font=("Arial", 18), fill="green")
    canvas.create_text(90, (y1 + y2) // 2, text=category, font=("Arial", 14, "bold"), fill="#333")


#Създаване на храните
canvas_food = tk.Canvas(root, width=WIDTH, height=400)
canvas_food.place(relx = 0.04,rely = 0.65)

images = []

food_items = []
with open("food", "r") as f:
    for row in f:
        items = row.strip().split(", ")
        items[1] = items[1].replace("\\n", "\n")
        ing = items[4].strip().split("; ")
        items[4] = ing
        food_items.append(items)

print(food_items)

for index, item in enumerate(food_items):
    create_food_box(item[0], str(item[1]), item[2], item[3], index)



selected_food_img = ttk.Label(root)
selected_food_img.place(relx=0.06, rely = 0.14)

selected_food_title = ttk.Label(root)
selected_food_title.place(relx=0.06, rely = 0.5)




root.mainloop()
