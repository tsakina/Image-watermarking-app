from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, ImageOps, ImageFont, ImageDraw



# class File:
#     def __init__(self, filename):
#         self.filename = filename


class Gui(Tk):
    def __init__(self, image):  #image is an App object
        super().__init__()
        self.image_object = image
        self.upload_button = Button(text="Upload", command=self.image_object.upload_file)
        self.upload_button.pack()

        self.canvas = Canvas(width=700, height=500, highlightthickness=0)
        image = self.image_object.get_image()
        self.canvas.create_image(400, 300, image=image)
        self.canvas.pack()

        self.mainloop()


class App:
    IMAGE_TKINTER = None

    def __init__(self):
        self.new_file = ""
        self.image_file = ""
        self.tkinter_file = ""
        self.window = Gui(self)

    def upload_file(self):
        file = askopenfilename(title="Browse File")
        if file:
            self.new_file += file
            self.image_file = Image.open(self.new_file)
            image = ImageOps.fit(image=self.image_file, size=(640, 374))
            IMAGE_TKINTER = ImageTk.PhotoImage(image=image)
            new_canvas = Canvas(self.window, width=800, height=600, highlightthickness=0)
            new_canvas.create_image(400, 300, image=IMAGE_TKINTER)
            new_canvas.pack()
        else:
            print("No file selected")

    def get_image(self, *args, **kwargs):
        print(self.new_file)
        if self.new_file != "":
            self.image_file = Image.open(self.new_file)
            image = ImageOps.fit(image=self.image_file, size=(640, 374))
            IMAGE_TKINTER = ImageTk.PhotoImage(image=image)
            return IMAGE_TKINTER


image_object = App()
# gui_image = Gui(image_object)


# gui_image.mainloop()

























# root = Tk()
#
# root.title('Font Families')
# fonts = list(font.families())
# fonts.sort()
#
#
# def populate(frame):
#     # Put in the font
#     listnumber = 1
#     for item in fonts:
#         label = "listlabel" + str(listnumber)
#         label = Label(frame, text=item, font=(item, 16)).pack()
#         listnumber += 1
#
#
# def onFrameConfigure(canvas):
#     # Reset the scroll region to encompass the inner frame
#     canvas.configure(scrollregion=canvas.bbox("all"))
#
#
# canvas = Canvas(root, borderwidth=0, background="#ffffff")
# frame = Frame(canvas, background="#ffffff")
# vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
# canvas.configure(yscrollcommand=vsb.set)
#
# vsb.pack(side="right", fill="y")
# canvas.pack(side="left", fill="both", expand=True)
# canvas.create_window((4,4), window=frame, anchor="nw")
#
# frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))
#
# populate(frame)
#
# root.mainloop()