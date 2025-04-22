import random
import time
from tkinter import *
from catcher import Catcher
from score import Score
from egg import Egg

tk = Tk()
tk.title("Game: Catcher")
tk.resizable(0, 0)
tk.wm_attributes("-topmost",True)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

score = Score(canvas)
catcher = Catcher(canvas, "blue", score)
tk.update()
time.sleep(3)

eggs = []
while 1:
    if random.randint(1, 100) == 1:
        eggs.append(Egg(canvas, "red", score))
    for egg in list(eggs):
        if egg.draw() == 'hit bottom':
            eggs.remove(egg)
    catcher.catch(eggs)
    catcher.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
    if score.lost >= 5:
        break

canvas.create_text(250, 200, text="Game Over!", fill="red", font=("Arial", 30))
canvas.create_text(250, 250, text="Score: " + str(score.score), fill="red", font=("Arial", 30))
tk.update()
time.sleep(1)