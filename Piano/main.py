from tkinter import *
from tkinter import ttk
from random import randint
from turtle import bgcolor, color
from PIL import Image, ImageTk
import numpy as np

movement = 10
speed = 200
# scol='./color/black.png'
# fcol='./color/black.png'

class Piano(Canvas):
    # global scol,fcol
    def __init__(self):
        super().__init__(
            width=600, 
            height=400, 
            background='#d2d2e0', 
            highlightthickness=0
        )
        global speed
        speed =200
        self.start_pos = (300, 100)
        self.obj = np.array([(300,100),])
        # self.food_pos = self.new_food()
        # self.direction = 'Right'
        self.score = 0
        self.img()
        self.objcolor()
        print("color")
        # self.foodimg()
        self.create_rectangle(
            10, 
            10, 
            590, 
            390, 
            outline='#FF0000'
            )
        self.create_rectangle(
            250, 
            300, 
            350, 
            340, 
            outline='#FF0000'
            )
        print("rec")
        self.bind_all('<Key>', self.on_key_press)
        self.pack()
        self.after(speed, self.perform_actions)
    def img(self):
        try:
            self.body = ImageTk.PhotoImage(Image.open('./color/yellow.png'))
            # self.food = ImageTk.PhotoImage(Image.open(fcol))
        except IOError as error:
            window.destroy()
            raise
    def objcolor(self):
        self.create_image(
                *self.obj[0],
                image=self.body,
                tag='obj'
                )

    def finish_game(self):
        self.delete(ALL)
        tryagain = Button(
            self,
            height=1,
            width=10,
            text="Try Again",
            command=playgame)
        tryagain.place(anchor='c',x=300,y=200)
        Scoreinform = Label(
            self,
            text = 'Your score is '+str(self.score),
            foreground="red",background='#d2d2e0')
        Scoreinform.place(anchor='c',x=300,y=170)
        # main = Button(
        #     self,
        #     height=1,
        #     width=10,
        #     text='Main menu',
        #     command=mainmenu)
        # main.place(anchor='c',x=300,y=230)
    def new_obj(self):
        food = randint(0,10)
        if food < 2:
            self.obj=np.append(self.obj,self.start_pos)
            self.create_image(
                *self.obj[-1],
                image=self.body,
                tag='obj'
                )
    def descend(self):
        for x in self.obj:
            x+=(0,10) 
        if (self.obj[0][1] > 380):
            np.delete(self.obj,0)
            self.finish_game()
        print (self.obj)
        for segment, position in zip(self.find_withtag('obj'), self.obj):
            self.coords(segment, position)
            # x_pos = randint(2, 58) * movement
            # y_pos = randint(2, 38) * movement
            # food_pos = (x_pos, y_pos)
            # if food_pos not in self.snake_pos:
            #     return food_pos
    def perform_actions(self):
        if (self.score>10):
            self.finish_game()
        self.descend()
        # self.new_obj()

        self.after(speed, self.perform_actions)
    def on_key_press(self, e):
        
        keypressed = e.keysym

        all_key = (
            'Up',
            )
        if (keypressed in all_key):
            if (self.obj[0][1] in range(300,340)):
                self.score +=1
                del(self.obj[0])
def playgame():
    global gamescreen
    for widgets in window.winfo_children():
        widgets.destroy()
    gamescreen = Piano()
class Mainmenu(Canvas):
    def __init__(self):
        super().__init__(
            width=600, 
            height=400, 
            background='#d2d2e0', 
            highlightthickness=0
        )
        Button(window,height=1,width=10,text='Play',command=playgame).place(anchor='c',x=300,y=190)



#main
window = Tk()
window.title('Snake Xenzia')
window.geometry("600x400")
window.resizable(False, False)
window.configure(bg='#d2d2e0')

gamescreen= Mainmenu()

window.mainloop()