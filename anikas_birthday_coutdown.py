from tkinter import *
import time
import datetime

bday=datetime.datetime(2024,5,26,0,0,0)
nyt = datetime.datetime.now()
timetobday = bday - nyt

win=Tk()
#Set the geometry
win.geometry("750x280")

canvas= Canvas(win, width= 1000, height= 750, bg="SpringGreen2")
canvas.pack()

def refresh():
 #Add a text in Canvas
    nyt = datetime.datetime.now()
    timetobday = bday - nyt
    canvas.delete("all")
    canvas.create_text(300, 50, text=' Anikas birthday is in {0}\n'.format(timetobday), fill="black", font=('Helvetica 15 bold'))
    canvas.pack()
    win.after(1000, refresh)


refresh()




win.mainloop()
#print("anika's birthdaty is in",timetobday)
#greeting = tk.Label(text="Hello, Tkinter")











































