from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askstring
from PIL import Image, ImageDraw, ImageFont

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing


def add_watermark():
    filename = askopenfilename(title='Select image:')  # show an "Open" dialog box and
    # return the path to the selected file
    image = Image.open(filename)

    text = askstring(title="Watermark text", prompt="Enter Watermark text")
    location = askstring(title="Watermark Location", prompt="LEFT/RIGHT/UP/DOWN/MIDDLE")

    return image.show()


add_watermark()

