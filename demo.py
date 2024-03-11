#library imports
import Main
from tkinter.ttk import *
from tkinter import *
import time

renderer = Main.renderer()
circle = Main.circle()

#init the window and viewport
master = Tk()
master.geometry(str(renderer.x) + 'x' + str(renderer.y+3))
master.title("Physics Engine: demo")

frame = Frame(master, width = renderer.x, height=renderer.y, bg="white")
frame.focus_set()
frame.pack(anchor=SW, side=LEFT)
viewport = Canvas(frame, width=renderer.x, height=renderer.y)
viewport.pack(side=TOP)

#main loop
def loop():
    start = time.time()
    viewport.create_rectangle(0,0,renderer.x,renderer.y, fill='white')
    objects = renderer.new_frame()
    for object in objects:
        viewport.create_oval(object[0]-object[2], object[1]-object[2], object[0]+object[2], object[1]+object[2], fill='green')
    frame_time = int((time.time() - start)*1000)
    if frame_time < 50:
        master.after(50-frame_time,loop)
    else:
        master.after(1,loop)

#call the loop
master.after(1,loop)
master.mainloop()
