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
        self.title("Title")
        self.bgcolor("black")
        self.root = self._canvas._root()
        self.menubar = tk.Menu(self.root)

class Menubar():
    def __init__(self, window, trt):
        # For use with tkinter widgets. Equivalent to self.root = tkinter.Tk()
        self.root = window._canvas._root()
        self.menubar = tk.Menu(self.root)
        # create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", command=window.__init__)
        filemenu.add_command(label="Save", command=self.dummy)
        filemenu.add_command(label="Open", command=self.dummy)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=window.bye)
        self.menubar.add_cascade(label="File", menu=filemenu)

        editmenu = tk.Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Background Color", command=self.bgcolor)
        self.menubar.add_cascade(label="Settings", menu=editmenu)
        self.menubar.add_command(label="About", command=self.about)
        toolbar = tk.Frame(self.root, bg = "white")
        tk.instertButt = tk.Button(toolbar, text="Fwd",command=
                                   trt.fwd).pack(side=tk.LEFT)
        tk.instertButt = tk.Button(toolbar, text="Bck",command=
                                   trt.bck).pack(side=tk.LEFT)
        tk.instertButt = tk.Button(toolbar, text="Lft",command=
                                   trt.lft).pack(side=tk.LEFT)
        tk.instertButt = tk.Button(toolbar, text="Rgt",command=
                                   trt.rgt).pack(side=tk.LEFT)
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)
        # display the menu
        self.root.config(menu=self.menubar)
        self.bgcolor = None
        self.var = tk.IntVar()

    def dummy(self):
        return

    def root2(self):
        self.bgcolor = tk.Tk()
        self.var = tk.IntVar(self.bgcolor,1)
        return self.bgcolor, self.var

    def bgcolor(self):
        bgcolor, var = self.root2()
        bgcolor.eval('tk::PlaceWindow %s center' % bgcolor.winfo_toplevel())
        colors = [
            ("white", 1),
            ("black", 2),
            ("blue", 3)]
        #self.var.set(1)
        tk.Label(bgcolor, text="Choose color:", justify = tk.CENTER,
                 padx=50).pack()
        for color, val in colors:
            tk.Radiobutton(bgcolor, text=color, width = 30, padx=30,
                           indicatoron=0, variable=var,
                           value=val).pack(anchor=tk.W)
        tk.Button(bgcolor, text="OK", padx=30,
                  command=self.color_choice).pack(anchor=tk.W)

    def color_choice(self):
        var = self.var.get()
        if var == 1:
            print("White")
            self.bgcolor.destroy()
        elif var == 2:
            print("Black")
            self.bgcolor.destroy()
        elif var == 3:
            print("Blue")
            self.bgcolor.destroy()
        else:
            print("None")
            self.bgcolor.destroy()

    def about(self):
        about = tk.Tk()
        about.eval('tk::PlaceWindow %s center' % about.winfo_toplevel())
        about.withdraw()
        tk.messagebox.showinfo("About",
                            """ This is just a tkinter test """)
        about.destroy()

class turtle(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.speed(5)
        #self.circle(50)
        self.speed = 10

    def hello(self):
        self.write("Hello!")

    def fwd(self):
        self.forward(100)

    def bck(self):
        self.back(100)

    def lft(self):
        self.left(90)

    def rgt(self):
        self.right(90)

    def move(self):
        self.forward(self.speed)
        if self.xcor() >= 100:
            self.speed = - 10
        if self.xcor() <= -100:
            self.speed = 10
        wn.ontimer(self.move,50)

wn = window()
tortoise = turtle()
menubar = Menubar(wn, tortoise)
#tortoise.move()
wn.mainloop()
