from tkinter import *
from tkinter.filedialog import Directory, askdirectory
from typing import Set, ValuesView
import pygame
import os
window = Tk()
window.title("موزیک پلیر")


def change_volume(a):
    a = volume.get()
    pygame.mixer.music.set_volume(a)


pygame.init()
pygame.mixer.init()


def play():

    pygame.mixer.music.load(play_list.get(ACTIVE))
    pygame.mixer.music.set_volume(volume.get())
    var.set(play_list.get(ACTIVE))
    pygame.mixer.music.play()


var = StringVar()
music_title = Label(window, fg="blue",bg="cyan",textvariable=var)

play_list = Listbox(fg="black",bg="brown")
play_list.pack()
volume = Scale(window, from_=0, to_=1, resolution=0.1,
               orient=HORIZONTAL, cursor="dot", command=change_volume,fg="green",bg="lightblue")
Label(window, text="sound",fg="red",bg="cyan").pack()
volume.pack(fill="x")
music_title.pack()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def sf():
    direct = askdirectory()
    os.chdir(direct)
    music_list = os.listdir(direct)

    for item in music_list:
        i = 0
        play_list.insert(i, item)
        i += 1


bmcl = Button(window, height=3, width=5, text="select folder", command=sf,fg="cyan",bg="orange")
bmcl.pack(fill="x")
bmp = Button(window, width=5, height=3, text="play", command=play,fg="cyan",bg="orange")
bmp.pack(fill="x")
bms = Button(window, height=3, width=5, text="stop", command=stop,fg="cyan",bg="orange")
bms.pack(fill="x")
bmp = Button(window, height=3, width=5, text="pause", command=pause,fg="cyan",bg="orange")
bmp.pack(fill="x")
bmup = Button(window, height=3, width=5, text="unpause", command=unpause,fg="cyan",bg="orange")
bmup.pack(fill="x")


window.resizable(height=False, width=False)
window.geometry("500x520")
window.mainloop()
