from tkinter import *
from tkinter import ttk
from random import randint
from turtle import bgcolor, color
from PIL import Image, ImageTk

movement = 10
speed = 200
scol='./Snake/color/black.png'
fcol='./Snake/color/black.png'

#Gamemain
class Snake(Canvas):
    global scol,fcol
    def __init__(self):
        super().__init__(
            width=600, 
            height=400, 
            background='#d2d2e0', 
            highlightthickness=0
        )
        global speed
        speed =200
        self.snake_pos = [(90, 90), (90, 100), (90, 100)]
        self.food_pos = self.new_food()
        self.direction = 'Right'

        self.score = 0

        self.img()
        self.snakebody()
        self.foodimg()
        self.create_rectangle(
            10, 
            10, 
            590, 
            390, 
            outline='#FF0000'
            )

        self.bind_all('<Key>', self.on_key_press)

        self.pack()

        self.after(speed, self.perform_actions)
    def img(self):
        try:
            self.body = ImageTk.PhotoImage(Image.open(scol))
            self.food = ImageTk.PhotoImage(Image.open(fcol))
        except IOError as error:
            window.destroy()
            raise
    def snakebody(self):
        for x_position, y_position in self.snake_pos:
            self.create_image(
                x_position, 
                y_position, 
                image=self.body, 
                tag='snake'
            )
    def foodimg(self):
        self.create_image(
            *self.food_pos, 
            image=self.food, 
            tag='food'
            )
    def finish_game(self):
        self.delete(ALL)
        tryagain = Button(
            self,
            height=1,
            width=10,
            text="Try Again",command=playgame)
        tryagain.place(anchor='c',x=300,y=200)
        Scoreinform = Label(
            self,
            text = 'Your score is '+str(self.score),
            foreground="red",background='#d2d2e0')
        Scoreinform.place(anchor='c',x=300,y=170)
        main=Button(
            self,
            height=1,
            width=10,
            text='Main menu',
            command=mainmenu)
        main.place(anchor='c',x=300,y=230)
        
    def consume_food(self):
        global speed
        if self.snake_pos[0] == self.food_pos:
            self.score += 1
            self.snake_pos.append(self.snake_pos[-1])

            self.create_image(
                *self.snake_pos[-1], 
                image=self.body, 
                tag='snake'
            )
            self.food_pos = self.new_food()
            self.coords(
                self.find_withtag('food'), 
                *self.food_pos
                )
            speed = int(speed//1.05)
    def boundary(self):
        head_x, head_y = self.snake_pos[0]

        return (
            head_x in (10, 590)
            or head_y in (10, 390)
            or (head_x, head_y) in self.snake_pos[1:]
        )
    def snake_movement(self):
        head_x, head_y = self.snake_pos[0]

        if self.direction == 'Left':
            new_head = (head_x - movement, head_y)
        elif self.direction == 'Right':
            new_head = (head_x + movement, head_y)
        elif self.direction == 'Down':
            new_head = (head_x, head_y + movement)
        elif self.direction == 'Up':
            new_head = (head_x, head_y - movement)

        self.snake_pos = [new_head] + self.snake_pos[:-1]
        for segment, position in zip(
            self.find_withtag('snake'),
            self.snake_pos):
            self.coords(segment, position)
    def on_key_press(self, e):
        
        new_direction = e.keysym

        all_directions = (
            'Up', 
            'Down', 
            'Left', 
            'Right'
            )
        opposites = (
            {'Up', 'Down'}, 
            {'Left', 'Right'}
            )

        if (
            new_direction in all_directions
            and {new_direction, self.direction} not in opposites
        ):
            self.direction = new_direction
    def perform_actions(self):
        if self.boundary():
            self.finish_game()

        self.consume_food()
        self.snake_movement()

        self.after(speed, self.perform_actions)
    def new_food(self):
        while True:
            x_pos = randint(2, 58) * movement
            y_pos = randint(2, 38) * movement
            food_pos = (x_pos, y_pos)
            if food_pos not in self.snake_pos:
                return food_pos

#Setting
class Settings(Canvas):
    def __init__(self):
        global scolor, fcolor
        super().__init__(
            width=600, 
            height=400, 
            background='#d2d2e0', 
            highlightthickness=0
        )
        Label(window,text = 'Snake color',foreground="red",background='#d2d2e0').place(anchor='c',x=300,y=140)
        scolor = ttk.Combobox(window, state='readonly',
                            values=[
                                    "black", 
                                    "red",
                                    "blue",
                                    "yellow"])
        scolor.place(anchor='c',x=300,y=160)
        scolor.current(0)
        Label(window,text = 'Food color',foreground="red",background='#d2d2e0').place(anchor='c',x=300,y=190)
        fcolor = ttk.Combobox(window, state='readonly',
                            values=[
                                    "black", 
                                    "red",
                                    "blue",
                                    "yellow"])
        fcolor.place(anchor='c',x=300,y=210)
        fcolor.current(0)
        Button(window,height=1,width=10,text='Back',command=mainmenu).place(anchor='c',x=300,y=240)
        scolor.bind('<<ComboboxSelected>>',Scolorchange)
        fcolor.bind('<<ComboboxSelected>>',Fcolorchange)
    #Changecolors
def Scolorchange(event):
    global scolor
    global scol
    scol = './color/'
    scol += str(scolor.get())
    scol +='.png'
def Fcolorchange(event):
    global fcolor
    global fcol
    fcol = './color/'
    fcol += str(fcolor.get())
    fcol +='.png'

#Mainmenu
class Mainmenu(Canvas):
    def __init__(self):
        super().__init__(
            width=600, 
            height=400, 
            background='#d2d2e0', 
            highlightthickness=0
        )
        Button(window,height=1,width=10,text='Play',command=playgame).place(anchor='c',x=300,y=190)
        Button(window,height=1,width=10,text='Settings',command=settings).place(anchor='c',x=300,y=220)

#Function
def playgame():
    global gamescreen
    for widgets in window.winfo_children():
        widgets.destroy()
    gamescreen = Snake()
def mainmenu():
    global gamescreen
    for widgets in window.winfo_children():
        widgets.destroy()
    gamescreen = Mainmenu()
def settings():
    global gamescreen
    for widgets in window.winfo_children():
        widgets.destroy()
    gamescreen = Settings()

#main
window = Tk()
window.title('Snake Xenzia')
window.geometry("600x400")
window.resizable(False, False)
window.configure(bg='#d2d2e0')

gamescreen= Mainmenu()

window.mainloop()