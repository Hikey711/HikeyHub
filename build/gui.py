
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

import webbrowser
lnk = webbrowser.open


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Hikey\Desktop\HikeyHub\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("673x524")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 524,
    width = 673,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    673.0,
    524.0,
    fill="#464484",
    outline="")

canvas.create_text(
    219.0,
    18.0,
    anchor="nw",
    text="Hikey Hub\n",
    fill="#828283",
    font=("Inter Bold", 48 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: lnk('https://www.youtube.com/@realhikey'),
    relief="flat",
    activebackground="#464484",
)
button_1.place(
    x=468.0,
    y=200.0,
    width=168.0,
    height=71.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: lnk('https://www.youtube.com/'),
    relief="flat",
    activebackground="#464484",
)
button_2.place(
    x=253.0,
    y=200.0,
    width=168.0,
    height=71.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: lnk('https://www.Github.com/'),
    relief="flat",
    activebackground="#464484",
)
button_3.place(
    x=36.0,
    y=200.0,
    width=168.0,
    height=71.0
)
window.resizable(False, False)
window.title("HikeyHub")
window.iconbitmap(r'C:\Users\Hikey\Desktop\HikeyHub\build\ICON.ico')
window.mainloop()
