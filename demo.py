#library imports
import Main
from tkinter.ttk import *
from tkinter import *
import time

renderer = Main.renderer()
circle = Main.circle()

frame_time = 1

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
    global frame_time
    viewport.create_rectangle(0,0,renderer.x,renderer.y, fill='white')
    start = time.time()
    objects = renderer.new_frame((50-frame_time)/1000)
    for object in objects:
        viewport.create_oval(object[0]-object[2], object[1]-object[2], object[0]+object[2], object[1]+object[2], fill='green')
    frame_time = int((time.time() - start))
    if frame_time < 50:
        master.after(50-frame_time,loop)
    else:
        frame_time = 1
        master.after(1,loop)

#call the loop
master.after(1,loop)
master.mainloop()
