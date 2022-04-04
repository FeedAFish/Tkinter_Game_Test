from tkinter import *
from tkinter import Tk, Canvas, Frame, BOTH, ttk
from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
import pyautogui
from pynput.keyboard import *
from keyboard import press
import sys
import random

pause = True
m = 0
get_key = Key.f3
pos = (0,0)

def on_press(key):
    global running, pause
    if key == get_key:
        Getpos()

lis = Listener(on_press=on_press)
lis.start()

#Wait
def waitfor(a):
    var = IntVar()
    window.after(a, var.set, 1)
    window.wait_variable(var)

#Main
def Gethunt():
    global value
    PMess.config(text='[Running] m = '+str(int(value.get())),foreground="red")
    pause = False
    m=int(value.get())
    i =0
    valuegem = [int(entry.get()) for entry in Gemchoices]
    chancegem= [int(entry.get()) for entry in Gemchances]
    while (not(pause) and (m>i)):
        PMess.config(text='[Running] m = '+str(int(value.get())) + '\n Remaining: '+str(m-i),foreground="red")
        pyautogui.click(pos)
        j= random.randint(1,2)
        textuse = ''
        useo = False
        for so in range(msongoc):
            if i % chancegem[so]==0:
                useo =True
                textuse += ( ' '+str(valuegem[so]))
        if useo:
            pyautogui.typewrite("owouse"+textuse)
            waitfor(500)
            press('enter')
            waitfor(1500)
        if i % 10 == 0:
            pyautogui.typewrite("owopray")
            waitfor(500)
            press('enter')
            waitfor(1500)
        if j==1:
            pyautogui.typewrite("owob")
            waitfor(500)
            press('enter')
            waitfor(random.randint(30000,60000))
        else:
            pyautogui.typewrite("owoh")
            waitfor(500)
            press('enter')
            waitfor(random.randint(30000,60000))
            i+=1
    PPause()

#Getpos
def Getpos():
    global pos
    pos = pyautogui.position()
    PPos.config(text=str(pos))

#Initial Window
window = Tk()
window.geometry("600x320")
window.title('Owo tool')

#Frametop
F1=Frame(window)
Label(F1, text = 'AUTO OwO').pack ()
canvas=Canvas(F1, width=2000, height=15)
canvas.pack()
canvas.create_line(0, 10, 2000, 10)
Label(F1, text = 'Press F3 to [Choose position]').pack()
PPos=Label(F1, text = '')
PPos.pack()
PMess=Label(F1, text = '[Pause]',foreground="red")
PMess.pack()
F1.pack()

#Pause
def PPause():
    global PMess
    pause = True
    PMess.config(text='[Pause]',foreground="red")

#Button
F2=Frame(window)
btn2 = Button(F2,height=1,width=10, text="Start",command=Gethunt)
btn1 = Button(F2,height=1,width=10, text="Stop",command=PPause)
btn2.grid(row=0,column=0,padx=20)
btn1.grid(row=0,column=1,padx=20)
F2.pack(pady=20)

#Input
F3=Frame(window)
Label(F3, text = '[Nhap so lan hunt]').grid(row=0,column=0,sticky="w")
value=IntVar()
MyEntryBox = Entry(F3, width=23,textvariable=value).grid(row=0,column=1,padx=20,sticky="e")
    #Combobox
Label(F3, text = '[Nhap so ngoc]').grid(row=1,column=0,sticky="w")
songoc = ttk.Combobox(F3, state='readonly',
                            values=[
                                    "0", 
                                    "1",
                                    "2",
                                    "3"])
songoc.grid(column=1, row=1,padx=20,sticky="e")
songoc.current(0)

F3.pack()
canvas=Canvas(window, width=2000, height=15)
canvas.pack()
canvas.create_line(0, 10, 2000, 10)

#Gemchoice
def Gemchoice(event):
    for widgets in F4.winfo_children():
        widgets.destroy()
    global msongoc
    msongoc=int(songoc.get())
    global Gemchoices
    Gemchoices = []
    global Gemchances
    Gemchances = []
    if int(msongoc)>0:
        for i in range(int(msongoc)):
            Label(F4, text = '[Nhap ngoc so '+ str(i+1)+']').grid(row=i,column=0,sticky="w")
            entry=Entry(F4, width=15)
            Gemchoices.append(entry)
            entry.grid(row=i,column=1,padx=20,sticky="w")
            Label(F4, text = '[Tac dung trong]').grid(row=i,column=2,sticky="w")
            entry=Entry(F4, width=15)
            Gemchances.append(entry)
            entry.grid(row=i,column=3,padx=20,sticky="w")

#F4 Main
F4=Frame(window)
songoc.bind('<<ComboboxSelected>>',Gemchoice)
F4.pack()

window.mainloop()
window.destroy()
lis.stop()
