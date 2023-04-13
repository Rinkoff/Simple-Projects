import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter


class ImageViewerApp:
    def __init__(self):
        self.current_img = None

        WINDOW_WIDTH = 1250
        WINDOW_HEIGHT = 700

        self.root = tk.Tk()
        self.root.title("Image Viewer")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

        self.images_collection = tk.Canvas(self.root, background="white")
        self.images_collection.place(relx=0.02, rely=0.02, relheight=0.64, relwidth=0.2)
        self.images_collection_sb = ttk.Scrollbar(
            self.images_collection, orient=tk.VERTICAL
        )
        self.images_collection_sb.pack(side="right", fill="y")
        self.images_collection.config(yscrollcommand=self.images_collection_sb.set)
        self.images_collection_sb.config(command=self.images_collection.yview)

        add_btn_image = Image.open("assets/Add.png")
        add_btn_image = add_btn_image.resize((100, 100))
        self.add_image_photo = ImageTk.PhotoImage(add_btn_image)
        self.add_image_btn = ttk.Button(
            self.images_collection, image=self.add_image_photo, command=self.add_image
        )
        self.add_image_btn.place(relx=0.02, rely=0.02, relwidth=0.90, relheight=0.4)

        self.image_lbl = ttk.Label(self.root)
        self.image_lbl.place(relx=0.23, rely=0.05, relwidth=0.637, relheight=0.58)

        self.info_lbl = ttk.Label(self.root, background="white")
        self.info_lbl.place(relx=0.02, rely=0.7, relwidth=0.186, relheight=0.27)

        blur_img = Image.open("assets/blur.jpg").resize((140, 180))
        blur_btn_img = ImageTk.PhotoImage(blur_img)
        self.blur_btn = ttk.Button(
            self.root,
            image=blur_btn_img,
            command=lambda: self.filter_img(ImageFilter.BLUR),
        )
        self.blur_btn.place(relx=0.23, rely=0.7, relwidth=0.12, relheight=0.27)

        sharpen_img = Image.open("assets/sharpen.jpg").resize((140, 180))
        sharpen_btn_img = ImageTk.PhotoImage(sharpen_img)
        self.sharpen_btn = ttk.Button(
            self.root,
            image=sharpen_btn_img,
            command=lambda: self.filter_img(ImageFilter.SHARPEN),
        )
        self.sharpen_btn.place(relx=0.36, rely=0.7, relwidth=0.12, relheight=0.27)

        contour_img = Image.open("assets/contour.jpg").resize((140, 180))
        contour_btn_img = ImageTk.PhotoImage(contour_img)
        self.contour_btn = ttk.Button(
            self.root,
            image=contour_btn_img,
            command=lambda: self.filter_img(ImageFilter.CONTOUR),
        )
        self.contour_btn.place(relx=0.49, rely=0.7, relwidth=0.12, relheight=0.27)

        emboss_img = Image.open("assets/emboss.jpg").resize((140, 180))
        emboss_btn_img = ImageTk.PhotoImage(emboss_img)
        self.emboss_btn = ttk.Button(
            self.root,
            image=emboss_btn_img,
            command=lambda: self.filter_img(ImageFilter.EMBOSS),
        )
        self.emboss_btn.place(relx=0.62, rely=0.7, relwidth=0.12, relheight=0.27)

        smooth_img = Image.open("assets/smooth.jpg").resize((140, 180))
        smooth_btn_img = ImageTk.PhotoImage(smooth_img)
        self.smooth_btn = ttk.Button(
            self.root,
            image=smooth_btn_img,
            command=lambda: self.filter_img(ImageFilter.SMOOTH),
        )
        self.smooth_btn.place(relx=0.75, rely=0.7, relwidth=0.12, relheight=0.27)

        ttk.Button(
            self.root,
            text="Rotate 90°",
            command=self.rotate_img,
        ).place(relx=0.87, rely=0.045, relwidth=0.12, relheight=0.12)
        ttk.Button(
            self.root,
            text="Flip Horizontal",
            command=lambda: self.flip(Image.FLIP_LEFT_RIGHT),
        ).place(relx=0.87, rely=0.18, relwidth=0.12, relheight=0.12)
        ttk.Button(
            self.root,
            text="Flip Vertical",
            command=lambda: self.flip(Image.FLIP_TOP_BOTTOM),
        ).place(relx=0.87, rely=0.315, relwidth=0.12, relheight=0.12)

        ttk.Label(self.root, text="Change size").place(relx=0.9, rely=0.47)

        self.img_width_entry = ttk.Entry(self.root, foreground="#808080")
        self.img_width_entry.place(relx=0.87, rely=0.51, relwidth=0.12, relheight=0.05)
        self.img_width_entry.insert(0, "Width")
        self.img_width_entry.bind(
            "<FocusIn>",
            lambda event: self.on_entry_click(
                event=event, entry=self.img_width_entry, text="Width"
            ),
        )
        self.img_width_entry.bind(
            "<FocusOut>",
            lambda event: self.on_focusout(
                event=event, entry=self.img_width_entry, text="Width"
            ),
        )

        self.img_height_entry = ttk.Entry(self.root, foreground="#808080")
        self.img_height_entry.place(relx=0.87, rely=0.58, relwidth=0.12, relheight=0.05)
        self.img_height_entry.insert(0, "Height")
        self.img_height_entry.bind(
            "<FocusIn>",
            lambda event: self.on_entry_click(
                event=event, entry=self.img_height_entry, text="Height"
            ),
        )
        self.img_height_entry.bind(
            "<FocusOut>",
            lambda event: self.on_focusout(
                event=event, entry=self.img_height_entry, text="Height"
            ),
        )

        self.error_lbl = ttk.Label(self.root, foreground="red")
        self.error_lbl.place(relx=0.88, rely=0.63)

        ttk.Button(self.root, text="Set", command=self.resize_img).place(
            relx=0.9, rely=0.66
        )

        self.save_btn = ttk.Button(self.root, text="Save As", command=self.save_img)
        self.save_btn.place(relx=0.875, rely=0.8, relwidth=0.12, relheight=0.12)

        self.root.mainloop()

    def on_entry_click(self, event, entry, text):
        if entry.get() == text:
            entry.delete(0, "end")
            entry.insert(0, "")
            entry.config(foreground="#000000")

    def on_focusout(self, event, entry, text):
        if entry.get() == "":
            entry.insert(0, text)
            entry.config(foreground="#808080")

    def add_image(self):
        self.file_path = filedialog.askopenfilename(
            title="Choose Image",
            filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg")],
        )
        if self.file_path:
            image = Image.open(self.file_path)
            image = image.resize((100, 100))
            image_btn = ImageTk.PhotoImage(image)
            button = ttk.Button(
                self.images_collection, command=lambda: self.show_image(self.file_path)
            )
            button.place(relx=0.02, rely=0.45, relwidth=0.90, relheight=0.4)
            button.config(image=image_btn)
            button.image = image_btn

    def show_image(self, image_path):
        self.img = Image.open(image_path).resize((400, 400))
        self.current_img = ImageTk.PhotoImage(self.img)
        self.image_lbl.config(image=self.current_img, anchor="center")
        self.show_parameters(self.file_path)

    def take_img_parameters(self, image):
        img = Image.open(image)
        img_name = os.path.basename(image).split(".")[0]
        img_size = img.size
        img_type = img.format
        img_mode = img.mode
        params = [img_name, img_size, img_type, img_mode]
        return params

    def show_parameters(self, image):
        params = self.take_img_parameters(image)
        separator = "-" * 50
        self.info_lbl.config(
            text=f"Image Name: {params[0]}\n"
            f"{separator}\n"
            f"Image Size: {params[1]}\n"
            f"{separator}\n"
            f"Image Type: {params[2]}\n"
            f"{separator}\n"
            f"Image Mode: {params[3]}\n"
            f"{separator}"
        )

    def rotate_img(self):
        self.img = self.img.rotate(90)
        self.current_img = ImageTk.PhotoImage(self.img)
        self.image_lbl.config(image=self.current_img, anchor="center")

    def flip(self, filter):
        self.img = self.img.transpose(filter)
        self.current_img = ImageTk.PhotoImage(self.img)
        self.image_lbl.config(image=self.current_img, anchor="center")

    def filter_img(self, filter):
        self.img = self.img.filter(filter)
        self.current_img = ImageTk.PhotoImage(self.img)
        self.image_lbl.config(image=self.current_img, anchor="center")

    def save_img(self):
        file_types = [("JPEG", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")]
        file = filedialog.asksaveasfile(
            mode="w", filetypes=file_types, defaultextension=".jpg"
        )
        if file is not None:
            self.img.save(file)
            file.close()

    def resize_img(self):
        try:
            width = int(self.img_width_entry.get())
            height = int(self.img_height_entry.get())
            self.error_lbl.config(text="")
            self.img = self.img.resize((width, height))
        except ValueError:
            self.error_lbl.config(text="Enter only numbers")


if __name__ == "__main__":
    ImageViewerApp()
