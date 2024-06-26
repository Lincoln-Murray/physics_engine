#library imports
import Main
from tkinter.ttk import *
from tkinter import *
import time

renderer = Main.renderer()
circle = Main.circle(renderer)
rect = Main.rectangle(renderer)

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
num_frames = 0
def loop():
    global frame_time, num_frames
    num_frames +=1
    if num_frames == 60:
        circle.delete()
    viewport.create_rectangle(0,0,renderer.x,renderer.y, fill='white')
    start = time.time()
    objects = renderer.new_frame((50-frame_time)/1000)
    for object in objects:
        if object[0] == 'circle':
            viewport.create_oval(object[3]-object[-1], object[4]-object[-1], object[3]+object[-1], object[4]+object[-1], fill='green')
        if object[0] == 'rectangle':
            viewport.create_rectangle(object[3], object[4], object[5], object[6], fill='red')
    frame_time = int((time.time() - start))
    if frame_time < 40:
        master.after(40-frame_time,loop)
    else:
        frame_time = 1
        master.after(1,loop)

#call the loop
master.after(1,loop)
master.mainloop()
