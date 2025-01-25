from tkinter import *
from shapes.circle import Circle
from shapes.rectangle import Rectangle
from shapes.triangle import Triangle



root = Tk()
# root.attributes("-fullscreen", True)
root.title("engine2D")
root.geometry("1920x1080")

# label = Label(text="Hello METANIT.COM")

width, height = root.wm_maxsize()

# canvas = Canvas(bg="white", width=width-200, height=height)
# canvas.pack(anchor=CENTER, expand=1)


btn_circle = Button(text='Circle', height=10, width=10, relief='groove')

btn_circle.pack()

# label.pack()  # размещаем метку в окне
root.mainloop()





