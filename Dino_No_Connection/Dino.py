from tkinter import *
from tkinter import ttk
from random import randint
from turtle import bgcolor, color
from PIL import Image, ImageTk


#Gamemain
class Dino(Canvas):
    def __init__(self):
        super().__init__(
            width=600, 
            height=400, 
            background='#d2d2e0', 
            highlightthickness=0
        )
        speed = 200
        self.snake_pos = [(90, 90), (90, 100), (100, 100),(100,110),(100,120),(110,100),(110,110),(120,120),(120,110),(120,100),(120,90),(120,80),(120,70),(130,70)]
        self.img()
        self.snakebody()
        self.create_rectangle(
            10, 
            10, 
            590, 
            390, 
            outline='#d9d8d7'
            )
        self.onair=False
        self.bind_all('<Key>', self.on_key_press)
        self.pack()
    def on_key_press(self, e):
        actions=e.keysym
        if     

    def img(self):
        try:
            self.body = ImageTk.PhotoImage(Image.open("./black.png"))
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
    def finish_game(self):
        self.delete(ALL)
        tryagain = Button(self,height=1,width=10, text="Try Again",command=playgame).place(anchor='c',x=300,y=200)
        Scoreinform = Label(self,text = 'Your score is '+str(self.score),foreground="red",background='#d2d2e0').place(anchor='c',x=300,y=170)
        main=Button(self,height=1,width=10,text='Main menu',command=mainmenu).place(anchor='c',x=300,y=230)

class Mainmenu(Canvas):
    def __init__(self):
        super().__init__(
            width=600, 
            height=400, 
            background='#d2d2e0', 
            highlightthickness=0
        )
        Button(window,height=1,width=10,text='Play',command=playgame).place(anchor='c',x=300,y=190)
def playgame():
    global gamescreen
    for widgets in window.winfo_children():
        widgets.destroy()
    gamescreen = Dino()
#Main
window = Tk()
window.title('Snake Xenzia')
window.geometry("600x400")
window.resizable(False, False)
window.configure(bg='#d2d2e0')

gamescreen= Mainmenu()

window.mainloop()