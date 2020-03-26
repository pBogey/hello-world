from turtle import Turtle, TurtleScreen, _Screen
import tkinter as tk

class window(_Screen):
    def __init__(self):
        super().__init__()
        TurtleScreen.__init__(self, self._canvas)
        if Turtle._screen is None:
            Turtle._screen = self
        self.setup(500,500)
        self.screensize(1000,1000)
        self.title("tkinter test")
        self.bgcolor("black")
        self.root = self._canvas._root()
        self.menubar = tk.Menu(self.root)

#root = tk.Tk()

class Menubar():
    def __init__(self, window):
        # For use with tkinter widgets. Equivalent to self.root = tkinter.Tk()
        self.root = window._canvas._root()
        self.menubar = tk.Menu(self.root)
        editmenu = tk.Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Background Color", command=self.bgcolor)
        self.menubar.add_cascade(label="Settings", menu=editmenu)
        self.root.config(menu=self.menubar)
        self.var = tk.IntVar()

    def bgcolor(self):
        global root
        #bgcolor = root
        #bgcolor = self.root
        bgcolor = tk.Tk()
        #bgcolor = tk.Tk()._root()
        bgcolor.eval('tk::PlaceWindow %s center' % bgcolor.winfo_toplevel())
        colors = [
            ("white", 1),
            ("black", 2),
            ("blue", 3)]
        var = self.var
        var = tk.IntVar(bgcolor,1)
        #self.var.set(1)
        tk.Label(bgcolor, text="Choose color:", justify = tk.CENTER,
                 padx=50).pack()
        for color, val in colors:
            tk.Radiobutton(bgcolor, text=color, width = 30, padx=30,
                           indicatoron=0, variable=var,
                           value=val).pack(anchor=tk.W)
        tk.Button(bgcolor, text="OK", padx=30,
                  command=lambda: print(var.get())).pack(anchor=tk.W)

    def color_choice(self):
        var = self.var.get()
        if var == 1:
            print("White")
        elif var == 2:
            print("Black")
        elif var == 3:
            print("Blue")
        else:
            print("None")

wn = window()
menubar = Menubar(wn)
wn.mainloop()
