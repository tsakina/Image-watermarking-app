from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageOps, ImageFont, ImageDraw

LIGHT_BEIGE = "#FFF4F4"


class ImageWatermarking:

    def __init__(self, window):
        self.filename = None
        self.image = None
        self.image_tkinter = None
        self.fonts = None
        self.window = window

    def upload(self):
        file = askopenfilename(title="Browse File",
                                        filetypes=(
                                                ("Text files", "*.txt"),
                                                ("Image Files", ("*.png", "*.jpeg")),
                                                ("All Files", "*.*")
                                                ))
        if file:
            return file
        else:
            return "No file selected"

    def get_image(self):
        self.filename = self.upload()
        image = Image.open(self.filename)
        return image

    def tkinter_image(self):
        image = self.get_image()
        self.image = ImageOps.fit(image=image, size=(640, 374))
        image_tkinter = ImageTk.PhotoImage(image=self.image)
        return image_tkinter

    def image_on_canvas(self):
        self.image_tkinter = self.tkinter_image()
        new_canvas = Canvas(self.window, width=800, height=600, bg=LIGHT_BEIGE, highlightthickness=0)
        new_canvas.create_image(400, 300, image=self.image_tkinter)
        new_canvas.grid(column=0, row=0, rowspan=2)

    # def choose_font(self):
    #     font = self.window.options.get().lower()
    #     text = self.window.text_entry.get()
    #     image_font = ImageFont.load(f"{font}.pil")
    #     draw_on_image = ImageDraw.Draw(self.image_tkinter)
    #     draw_on_image.text((28, 36), text, font=image_font, fill="brown")
