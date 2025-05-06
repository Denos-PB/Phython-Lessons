import time
from config import *
from player import Player
from target import Target
class Game:
    def __init__(self):
        self.target = None
        self.player = None
        self.tk = tk.Tk()
        self.tk.title("Reach the target")
        self.tk.resizable(0,0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = tk.Canvas(self.tk,width=SCREEN_WIDTH,height=SCREEN_HEIGT, bg=COLOR_BG)
        self.canvas.pack()
        self.create_game_object()
        self.tk.update()
        self.running = True


    def create_game_object(self):
        self.player = Player(self.canvas,50,50,20,30,"blue")
        self.tk.bind("<KeyPress-Up>",self.player.move_up)
        self.tk.bind("<KeyPress-Down>", self.player.move_down)
        self.tk.bind("<KeyPress-Left>", self.player.move_left)
        self.tk.bind("<KeyPress-Right>", self.player.move_right)
        self.target = Target(self.canvas,15,"red")

    def mainloop(self):
        while self.running:
            self.player.move()
            self.check_collisons()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)

    def check_collisons(self):
        if self.player.collides_width(self.target):
            self.canvas.create_text(SCREEN_WIDTH/2, SCREEN_HEIGT/2, 
            text="Game won", font=("Arial", 30), fill="green")
            self.tk.update()
            time.sleep(3)
            self.running = False
