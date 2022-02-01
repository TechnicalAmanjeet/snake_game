from turtle import Turtle
ALIGN_TEXT = "center"
FONT_TYPE = "Arial"
FONT_SIZE = 14
FONT_WEIGHT = "bold"
FONT = (FONT_TYPE, FONT_SIZE, FONT_WEIGHT)

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        output = f"Score : {self.score}"
        self.penup()
        self.color("white")
        self.hideturtle()
        # self.shape("circle")
        # self.shapesize(0.001)
        # self.write(arg=output, move=(0, 200), align="center", )
        self.goto((0, 275))
        self.write(arg=output, align=ALIGN_TEXT, font=FONT)
        # self.write((0, 150), True)

    def refresh(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto((0, 0))
        self.write(arg="Game Over!!!", align=ALIGN_TEXT, font=FONT)
        self.goto((0, -30))
        output = f"Score : {self.score}"
        self.write(arg=output, align=ALIGN_TEXT, font=FONT)
