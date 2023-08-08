from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageOps, ImageFont, ImageDraw
# from gui import App
from another_gui import App
from new import ImageWatermarking

# code to upload a picture or file from computer
GREY = "#9BABB8"
LIGHT_BEIGE = "#FFF4F4"
DARK_BEIGE = "#D7C0AE"
BROWN = "#967E76"
FONT_NAME = "Courier"
img = None
image_tk = None
FONT_PATH = "/Library/Fonts/"

app = App()

#
# file = askopenfilename(title="Browse File")
# if file:
# object = App(file)  this class has a function to get the image on canvas and initializes it in the beginning itself.
# else:
# message = "File not found"
# gui.message(message-string)
#


# new_picture = ImageWatermarking()
# ---------------------------- UPLOAD AN IMAGE FILE ------------------------------- #
# def upload(*args):
#     filename = askopenfilename(title="Browse File",
#                                filetypes=(
#                                 ("Text files", "*.txt"),
#                                 ("Image Files", ("*.png", "*.jpeg")),
#                                 ("All Files", "*.*")
#                                 ))
#     if filename:
#         print(filename)
#         global img, image_tk
#         new_canvas = Canvas(window, width=800, height=600, bg=LIGHT_BEIGE, highlightthickness=0)
#         img = Image.open(filename)
#         # if img.size > (650, 380):
#         #     img = img.resize((640, 374), Image.LANCZOS)
#         # standard image size = (1280, 720)
#         img = ImageOps.fit(image=img, size=(640, 374))
#         image_tk = ImageTk.PhotoImage(image=img)
#         new_canvas.create_image(400, 300, image=image_tk)
#         new_canvas.grid(column=0, row=0, rowspan=2)
#
#         font = options.get()
#         text = text_entry.get()
#         font_to_use = ImageFont.truetype(font=f"{FONT_PATH}{font}.ttf", size=10)
#         draw_on_image = ImageDraw.Draw(img)
#         draw_on_image.text((28, 36), text, font=font_to_use, fill=BROWN)
#
#     else:
#         print("No file selected")
#
#     return filename
#
#
# # ---------------------------- CHOSE A FONT FOR THE WATER-MARK------------------------------- #
# def choose_font(*args):
#     font = options.get()
#     text = text_entry.get()
#     img = Image.open("/Users/sakina/Downloads/city.jpeg")
#     font_to_use = ImageFont.truetype(font=f"{FONT_PATH}{font}.ttf", size=10)
#     draw_on_image = ImageDraw.Draw(img)
#     draw_on_image.text((28, 36), text, font=font_to_use, fill=BROWN)
#
#
# # ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title("Image WaterMarking App")
# window.config(bg=LIGHT_BEIGE, padx=50, pady=50)
#
# # Fonts
# fonts = list(font.families())
# print(fonts)
#
# # Canvas
# canvas = Canvas(window, width=700, height=500, highlightthickness=0)
# # img = Image.open(filepath)
# # img_tk = ImageTk.PhotoImage(image=img)
# # canvas_image = canvas.create_image(400, 300, image=img_tk)
# canvas.grid(column=0, row=0, rowspan=2)
#
# # Label
# text_label = Label(text="Logo", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE, font=(FONT_NAME, 20, "bold"))
# text_label.grid(column=1, row=0)
# font_label = Label(text="Font", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE, font=(FONT_NAME, 20, "bold"))
# font_label.grid(column=1, row=1)
#
# # Entry
# text_entry = Entry()
# text_entry.grid(column=2, row=0)
#
# # Option Menu
# options = StringVar(window)
# font_entry = OptionMenu(window, options, *fonts)
# options.trace("w", new_picture.upload)
# font_entry.grid(column=2, row=1)
#
# # Button
# upload_button = Button(text="Upload", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE,
#                        font=(FONT_NAME, 18, "bold"), command=new_picture.upload)
# upload_button.grid(column=0, row=3)
# save_button = Button(text="Save", bg=LIGHT_BEIGE, fg=GREY, highlightbackground=LIGHT_BEIGE,
#                      font=(FONT_NAME, 18, "bold"))
# save_button.grid(column=1, row=3)
#
#
# window.mainloop()
