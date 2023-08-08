from tkinter import *
from tkinter import font
from PIL import Image, ImageTk, ImageOps, ImageFont, ImageDraw
from new import ImageWatermarking

GREY = "#9BABB8"
LIGHT_BEIGE = "#FFF4F4"
DARK_BEIGE = "#D7C0AE"
BROWN = "#967E76"
FONT_NAME = "Courier"


class App:

    def __init__(self):

        window = Tk()
        self.app = ImageWatermarking(window)
        window.title("Image WaterMarking App")
        window.config(bg=LIGHT_BEIGE, padx=50, pady=50)
 
        # Fonts
        fonts = list(font.families())
        print(fonts)

        # Canvas
        canvas = Canvas(window, width=700, height=500, highlightthickness=0)
        # img = Image.open(filepath)
        # img_tk = ImageTk.PhotoImage(image=img)
        # canvas_image = canvas.create_image(400, 300, image=img_tk)
        canvas.grid(column=0, row=0, rowspan=2)

        # Label
        text_label = Label(text="Logo", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE,
                           font=(FONT_NAME, 20, "bold"))
        text_label.grid(column=1, row=0)
        font_label = Label(text="Font", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE,
                           font=(FONT_NAME, 20, "bold"))
        font_label.grid(column=1, row=1)

        # Entry
        text_entry = Entry()
        text_entry.grid(column=2, row=0)

        # Option Menu
        options = StringVar(window)
        font_entry = OptionMenu(window, options, *fonts)
        options.trace("w", self.app.image_on_canvas())
        font_entry.grid(column=2, row=1)

        # Button
        upload_button = Button(text="Upload", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE,
                               font=(FONT_NAME, 18, "bold"), command=self.app.image_on_canvas)
        upload_button.grid(column=0, row=3)
        save_button = Button(text="Save", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE,
                             font=(FONT_NAME, 18, "bold"))
        save_button.grid(column=1, row=3)

        window.mainloop()



