class Score:
    def __init__(self, canvas):
        self.canvas = canvas
        self.score = 0
        self.lost = 0
        self.text = ""
        self.show_text()
    def show_text(self):
        if(self.text == ""):
            self.text = self.canvas.create_text(350,10, text = "Catch: 0 Lost: 0 ", font = ("Helvetica", 16))
        else:
            self.canvas.itemconfig(self.text, text = f"Catch:{str(self.score)} Lost:{str(self.lost)}")
    def catched_egg(self):
        self.score += 1
        self.show_text()
    def lost_egg(self):
        self.lost += 1
        self.show_text()