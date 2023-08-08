from tkinter import *
from tkinter import font
from PIL import Image, ImageTk, ImageOps, ImageFont, ImageDraw
from new import ImageWatermarking

GREY = "#9BABB8"
LIGHT_BEIGE = "#FFF4F4"
DARK_BEIGE = "#D7C0AE"
BROWN = "#967E76"
FONT_NAME = "Courier"


class App(Tk):

    def __init__(self):
        super().__init__()
        self.title("IWA")
        self.app = ImageWatermarking(self)
        self.config(bg=LIGHT_BEIGE, padx=50, pady=50)

        # Fonts
        self.fonts = list(font.families())

        # Canvas
        self.canvas = Canvas(self, width=700, height=500, highlightthickness=0)
        # img = Image.open(filepath)
        # img_tk = ImageTk.PhotoImage(image=img)
        # canvas_image = canvas.create_image(400, 300, image=img_tk)
        self.canvas.grid(column=0, row=0, rowspan=2)

        # Label
        self.text_label = Label(text="Logo", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE,
                                font=(FONT_NAME, 20, "bold"))
        self.text_label.grid(column=1, row=0)
        self.font_label = Label(text="Font", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE,
                           font=(FONT_NAME, 20, "bold"))
        self.font_label.grid(column=1, row=1)

        # Entry
        self.text_entry = Entry()
        self.text_entry.grid(column=2, row=0)

        # Option Menu
        self.options = StringVar(self)
        self.font_entry = OptionMenu(self, self.options, *self.fonts)
        self.options.trace("w", self.app.image_on_canvas())
        self.font_entry.grid(column=2, row=1)

        # Button
        self.upload_button = Button(text="Upload", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE,
                                    font=(FONT_NAME, 18, "bold"), command=self.app.upload)
        self.upload_button.grid(column=0, row=3)
        self.save_button = Button(text="Save", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE,
                                  font=(FONT_NAME, 18, "bold"))
        self.save_button.grid(column=1, row=3)

        self.mainloop()