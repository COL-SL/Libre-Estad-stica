from Tkinter import *


class GUI:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        #status bar
        self.bar = Frame(root, relief=RIDGE, borderwidth=5)
        self.bar.pack(side=TOP)

        self.iconPath = r"/home/manueldavid/Escritorio/Programa_estadistica/imagenes/lararov_6.gif"
        self.icon = PhotoImage(Image.open(self.iconPath))
        self.icon_size = Label(self.bar, image = self.icon)
        self.icon_size.pack(side=LEFT)

root = Tk()


app = GUI(root)

root.mainloop()