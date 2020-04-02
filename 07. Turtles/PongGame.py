from turtle import Turtle, _Screen, TurtleScreen
from random import choice, randrange, randint
import tkinter as tk
import random

class Field(_Screen):
    def __init__(self, width = 1024, height = 600):
        """ Create pong court of width x height """
        # Get __init__ from _Screen
        super().__init__()
        # Get __init__ from TurtleScreen (parent class of _Screen)
        TurtleScreen.__init__(self, self._canvas)
        if Turtle._screen is None:
            Turtle._screen = self
        self.width = width
        self.height = height
        self.setup(self.width+100,self.height+50)
        self.screensize(self.width,self.height)
        self.title("Pong")
        self.bgcolor("black")
        self.delay(8)
        # Define size of score bar, above the play field
        self.score_height = self.height/10
        # Offset 0 axis line, due to score bar
        self.yzero = -(self.height/2 - (self.height-self.score_height)/2)
        self.top_border = ((self.height/2)-
                           self.score_height)
        self.low_border = -self.height/2
        self.right_border = self.width/2
        self.left_border = -self.width/2

class Menubar(Field):
    def __init__(self, game):
        # For use with tkinter widgets. Equivalent to self.root = tkinter.Tk()
        self.game = game
        self.root = self.game.court._canvas._root()
        self.menubar = tk.Menu(self.root)
        # create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New", command=game.restart)
        filemenu.add_command(label="Save", command=game.over)
        filemenu.add_command(label="Open", command=game.reset)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=game.qt)
        self.menubar.add_cascade(label="File", menu=filemenu)

        editmenu = tk.Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Game Difficulty", command=self.difficulty)
        editmenu.add_command(label="Player 1 color", command=self.player_color)
        editmenu.add_command(label="Player 2 color", command=self.player_color)
        self.menubar.add_cascade(label="Settings", menu=editmenu)
        
        # Some information about this game
        self.menubar.add_command(label="About", command=self.about)
        # display the menu
        self.root.config(menu=self.menubar)
        # Initialize variables for radiobuttons
        self.radio_root = None
        self.radio_var = None

    def radioroot(self):
        """ Create tkinter root and variable holder for radiobutton menu """
        # This is the only solution I found to retrieve the radiobutton var
        # in a clean way, using the current program arhitecture
        self.radio_root = tk.Tk()
        self.radio_var = tk.IntVar(self.radio_root,1)
        return self.radio_root, self.radio_var

    def dummy(self):
        return

    def set_diff(self):
        """ Modify game difficulty as per user choice """
        var = self.radio_var.get()
        vel = ((game.court.top_border - game.court.yzero)
               / 30*game.ball.shapesize()[1])
        if var == 1:
            print("Easy")
            self.game.p1.clock = 34
            self.game.p1.cpu_ai_lvl = 1
            self.game.p2.clock = 34
            self.game.p2.cpu_ai_lvl = 1
            self.game.ball.velocity = vel * 0.75
            self.radio_root.destroy()
        elif var == 2:
            print("Medium")
            self.game.p1.clock = 25
            self.game.p1.cpu_ai_lvl = 2
            self.game.p2.clock = 25
            self.game.p2.cpu_ai_lvl = 2
            self.game.ball.velocity = vel * 1
            self.radio_root.destroy()
        elif var == 3:
            print("Hard")
            self.game.p1.clock = 17
            self.game.p1.cpu_ai_lvl = 3
            self.game.p2.clock = 17
            self.game.p2.cpu_ai_lvl = 3
            self.game.ball.velocity = vel * 1.5
            self.radio_root.destroy()
        else:
            print("None")

    def difficulty(self):
        """ Create multiple choice menu for game difficulty """
        # Create options window
        difficulty, var = self.radioroot()
        difficulty.eval('tk::PlaceWindow %s center' %
                        difficulty.winfo_toplevel())
        # Create list of options
        diff_list = [
            ("Easy", 1),
            ("Medium", 2),
            ("Hard", 3)]
        tk.Label(difficulty, text="Choose game difficulty:",
                 justify = tk.CENTER, padx=50).pack()
        # Create options
        for diff, val in diff_list:
            tk.Radiobutton(difficulty, text=diff, width = 30, padx=30,
                           indicatoron=0,variable=var,
                           value=val).pack(anchor=tk.W)
        tk.Button(difficulty, text="OK", padx=30,
                  command=self.set_diff).pack(anchor=tk.W)
        
    def player_color(self):
        """ Create multiple choice menu for player color """
        # Create options window
        p_color.eval('tk::PlaceWindow %s center' % p_color.winfo_toplevel())
        # Create list of options
        colors = [
            ("White", 1),
            ("Yellow", 2),
            ("Pink", 3)]
        tk.Label(p_color, text="Choose player 1 color:", justify = tk.CENTER, padx=50).pack()
        # Create options
        for val, diff in colors:
            tk.Radiobutton(p_color, text=val, width = 30, padx=30, indicatoron=0,
                           variable=v, value=diff).pack(anchor=tk.W)

    def p1_color(self):
        return

    def p2_color(self):
        return

    def about(self):
        """ Information about the game """
        about = tk.Tk()
        about.eval('tk::PlaceWindow %s center' % about.winfo_toplevel())
        about.withdraw()
        tk.messagebox.showinfo("About Pong",
                            """ This game is Bogdan Prădatu's first Python project.
\nEnjoy! """)
        about.destroy()

class Ball(Turtle):
    def __init__(self, court, velocity = None, size = 1, color = "white"):
        """ Create pong ball """
        super().__init__(shape="circle",visible=False)
        self.color(color)
        self.speed(0)
        self.penup()
        self.shapesize(size,size)
        self.setposition(0,field.yzero)
        self.st()
        if velocity == None:
        # Evenly space field to not allow ball to cross outside of borders
            self.velocity = ((court.top_border-court.yzero) /
                             30*self.shapesize()[1])
        else:
            self.velocity = velocity
        self.dirrection = 0
        self.offset = self.shapesize()[0]*10
        self.court = court
        self.moving = False

    def player_collision(self,player):
        """ Check for collision between ball and player """
        if player.xcor() > 0:
            if (self.xcor() + self.offset >= player.xcor() - player.width and
                self.ycor() - self.offset <= player.ycor() + player.height and
                self.ycor() + self.offset >= player.ycor() - player.height):
                return True
        elif player.xcor() < 0:
            if (self.xcor() - self.offset <= player.xcor() + player.width and
                self.ycor() - self.offset <= player.ycor() + player.height and
                self.ycor() + self.offset >= player.ycor() - player.height):
                return True
        return False
        
    def court_collision(self):
        """ Check for collision between ball and court borders """
        return not (self.court.low_border + self.offset
                    <= self.ycor()
                    <= self.court.top_border - self.offset)

    def out_left(self):
        """ Check for out on left side of court """
        if self.xcor() <= self.court.left_border: return True
        return False

    def out_right(self):
        """ Check for out on right side of court """
        if self.xcor() >= self.court.right_border: return True
        return False        

class Player(Turtle):
    def __init__(self, ball, x=0, y=0, color="white", up=None, down=None):
        """ Create player paddle, at position (x,y),
            with control keys up & down.
            Use "color" to personalize player.
        """
        super().__init__(shape="square",visible=False)
        self.color(color)
        self.speed(0)
        self.penup()
        # setup player paddle
        self.shapesize(0.5,5)
        # Rotate turtle, to allow the use of forward method
        self.setheading(90)
        self.setposition(x,y)
        self.st()
        self.score = 0
        self.height = self.shapesize()[1]*10
        self.width = self.shapesize()[0]*10
        self.ball = ball
        self.court = ball.court
        # Evenly space field to not allow player to cross outside of borders
        self.velocity = ((field.height-field.score_height)/2)/(self.height/2)
        # Player accuracy when aiming for the ball
        self.cpu_ai_fac = 1
        self.cpu_ai_lvl = 1
        # Player reaction speed
        self.clock = 17
        self.upkey = up
        self.downkey = down
        # Alow user to control player by mouse. Function not currently working well.
        self.ondrag(self.drag)
        
    def cpu(self):
        """ Create simple AI for single player mode """
        if self.cpu_ai_lvl == 1:
            self.cpu_ai_fac = random.choice([1.1,1.15,1.2,1.25,1.3])
        elif self.cpu_ai_lvl == 2:
            self.cpu_ai_fac = random.choice([1,1.05,1.1,1.15,1.2])
        elif self.cpu_ai_lvl == 3:
            self.cpu_ai_fac = random.choice([0.9,0.95,1,1.15,1.1])
        else:
            self.cpu_ai_fac = random.choice([0.9,0.95,1,1.05,
                                             1.1,1.15,1.2,1.25,1.3])
        if self.ball.moving:
            if ((self.xcor() < 0 and
                 self.xcor() + self.ball.xcor() <= -self.court.width*0.8) or
                self.xcor() > 0 and
                self.xcor() - self.ball.xcor() <= self.court.width*0.2):
                if self.ycor() < self.ball.ycor()-self.height*self.cpu_ai_fac:
                    self.up()
                elif self.ycor() > self.ball.ycor()+self.height*self.cpu_ai_fac:
                    self.down()
            else:
                if self.ycor() < self.court.yzero-self.height:
                    self.up()
                elif self.ycor() > self.court.yzero+self.height:
                    self.down()
        self.court.ontimer(self.cpu,self.clock)        

    def drag(self,x,y):
        """ Alow to control player paddle with mouse """
        self.ondrag(None) # Disable event handler to avoid recursion
        if y >= self.court.top_border-self.height:
            y = self.court.top_border-self.height
        if y <= self.court.low_border+self.height:
            y = self.court.low_border+self.height
        self.goto(self.xcor(),y)
        self.ondrag(self.drag) # Reactivate event handler

    def up(self):
        """ Move player paddle up """
        if (self.ycor()+self.height <= self.court.top_border):
            self.forward(self.velocity)
        
    def down(self):
        """ Move player paddle down """
        if self.ycor()-self.height >= self.court.low_border:
            self.forward(-self.velocity)

class Game:
    def __init__(self, ball, player_1, player_2, difficulty=1):
        """ Initialize game parameters """
        # Difficulty = increase in ball speed
        self.difficulty = difficulty
        # initialize participants
        self.ball = ball
        self.p1 = player_1
        self.p2 = player_2
        self.court = ball.court
        # Parameters for pause method
        self.pause_state = False
        self.pause_count = 0
        # Number of human players
        self.humans = 0
        # Setup event handlers
        self.court.listen()
        self.court.onkeypress(self.qt, "Escape")
        self.court.onkeypress(self.pause, "p")
        self.court.onkeypress(self.p1.up, self.p1.upkey)
        self.court.onkeypress(self.p1.down, self.p1.downkey)
        self.court.onkeypress(self.p2.up, self.p2.upkey)
        self.court.onkeypress(self.p2.down, self.p2.downkey)

    def playing(self):
        """ Make the ball move """
        if not self.pause_state:
            self.ball.forward(self.ball.velocity)
            # Check for paddle collision
            if (self.ball.player_collision(self.p1) or
                self.ball.player_collision(self.p2)):
                self.ball.setheading(180 - self.ball.heading())
            # Bounce from upper or lower border
            if self.ball.court_collision():
                self.ball.setheading(-self.ball.heading())
            # Check for ball out of field and update player score
            elif self.ball.out_right():
                self.reset()
                self.p2.score += 1
                score.update()
                self.difficulty += 0.1
            elif self.ball.out_left():
                self.reset()
                self.p1.score += 1
                score.update()
                self.difficulty += 0.1
        if self.p1.score < 11 and self.p2.score < 11:
            self.court.ontimer(self.playing,17)
        else:
            game.over()

    def reset(self):
        """ Reset ball and player paddle position """
        self.ball.setposition(0,self.court.yzero)
        self.p1.setposition(player1.xcor(),self.court.yzero)
        self.p2.setposition(player2.xcor(),self.court.yzero)
        self.ball.dirrection = choice([0,180])   # Left or right
        self.ball.setheading(self.ball.dirrection+randrange(-80,80))

    def restart(self):
        """ Restart game """
        self.reset()
        self.pause_state = True
        self.p1.score = 0
        self.p2.score = 0
        score.update()
        self.difficulty = 0

    def over(self):
        """ Game Over """
        if self.p1.score == 11:
            text = f"Player 1 has won!"
        elif self.p2.score == 11:
            text = f"Player 2 has won!"
        else:
            text = ""
        wn = tk.Tk()
        wn.eval('tk::PlaceWindow %s center' % wn.winfo_toplevel())
        wn.withdraw()
        answer = tk.messagebox.askyesno("Game over", text+"\nDo you want to play again?")
        if answer == True:
            wn.destroy()
            self.restart()
        else:
            wn.destroy()

    def qt(self):
        """ Quit game """
        prompt = tk.Tk()
        prompt.eval('tk::PlaceWindow %s center' % prompt.winfo_toplevel())
        prompt.withdraw()
        answer = tk.messagebox.askyesno("Quit", "Are you sure you want to quit?")
        if answer == True:
            prompt.destroy()
            self.court.bye()
        else:
            prompt.destroy()

    def pause(self):
        """ Pause game """
        if self.pause_count % 2 == 0:
            self.pause_state = True
            self.ball.moving = False
            self.pause_count += 1
            print("Pause:",self.pause_state)
        else:
            self.pause_state = False
            self.ball.moving = True
            self.pause_count += 1
            print("Pause:",self.pause_state)

class Menu(Turtle):
    def __init__(self, game):
        """ Initialize game menu """
        super().__init__(visible=False)
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(0.1,1)
        self.speed(0)
        self.penup()
        self.pensize(3)
        self.game = game
        self.court = self.game.court
        self.court.onscreenclick(self.click)

    def border(self):
        """ Create court border """
        # Draw lower border
        self.penup()
        self.goto(-self.court.width,-self.court.height/2)
        self.pendown()
        self.goto(self.court.width,-self.court.height/2)
        # Draw upper border
        self.penup()
        self.goto(-self.court.width,self.court.height/
                  2-self.court.score_height)
        self.pendown()
        self.goto(self.court.width,self.court.height/
                  2-self.court.score_height)
        self.penup()
        self.goto(0,self.court.height/2-self.court.score_height)
        self.pendown()
        self.goto(0,-self.court.height/2)
        self.penup()

    def play(self):
        """ Create play button """
        self.font_size = int(self.court.score_height/4)
        self.goto(-self.court.width/2,
                  self.court.height/2-self.court.score_height/2)
        self.write("Play",font=("Monospace",self.font_size,"bold"))

    def pause(self):
        """ Create pause button """
        self.goto(-5,self.court.height/2-self.court.score_height/2)
        self.stamp()
        self.goto(5,self.court.height/2-self.court.score_height/2)
        self.stamp()

    def click(self, x, y):
        """ Assign menu function on mouse click """
        print(x,y)
        if (x <= -self.court.width/2+self.court.width/2/10 and
            x >= -self.court.width/2 and
            y >= self.court.height/2-self.court.score_height/2 and
            y <= self.court.height/2):
            self.goto(-self.court.width/2,
                      self.court.height/2-self.court.score_height/2)
            self.color("green")
            self.write("Play",font=("Monospace",self.font_size,"bold"))
            self.game.reset()
            self.game.pause_state = False
            self.game.playing()
            self.game.ball.moving = True
            if self.game.humans == 1:
                self.game.p2.cpu()
            elif self.game.humans == 0:
                self.game.p1.cpu()
                self.game.p2.cpu()
            self.undo()
        if (x <= 5 and x >= -5 and
            y >= self.court.height/2-self.court.score_height and
            y <= self.court.height/2):
            self.game.pause()

class Score(Turtle):
    def __init__(self, player_1, player_2):
        """ Initialize player score """
        super().__init__(visible=False)
        self.speed(0)
        self.penup()
        self.color("white")
        self.p1 = player_1
        self.p2 = player2
        # Draw score
        self.font_size = field.height//15
        self.spacing = field.width/10
        self.goto(-self.spacing,field.height/2-field.score_height)
        self.write(self.p2.score,font=("Monospace",self.font_size,"bold")) 
        self.goto(self.spacing-self.font_size*0.6,
                  field.height/2-field.score_height)
        self.write(self.p1.score,font=("Monospace",self.font_size,"bold"))

    def update(self):
        """ Update player score """
        # Clear the previous score
        for i in range(3):
            self.undo()
        # And write the new one
        self.write(self.p2.score,font=("Monospace",self.font_size,"bold")) 
        self.goto(self.spacing-self.font_size*0.6,
                  field.height/2-field.score_height)
        self.write(self.p1.score,font=("Monospace",self.font_size,"bold"))

if __name__ == "__main__":
    field = Field(1280,720)
    ball = Ball(field)
    player1 = Player(ball, field.width/2, field.yzero, up = "Up", down = "Down")
    player2 = Player(ball, -field.width/2, field.yzero, up = "w", down = "s")
    score = Score(player1, player2)
    game = Game(ball, player1, player2)
    menubar = Menubar(game)
    menu = Menu(game)
    menu.border()
    menu.pause()
    menu.play()
    field.mainloop()

