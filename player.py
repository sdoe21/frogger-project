import turtle

class Player(turtle.Turtle):
    def __init__(self, screen_height, margin, step):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")

        self.screen_height = screen_height
        self.margin = margin
        self.step = step

        self.reset_position()

    def move_up(self):
        self.sety(self.ycor() + self.step)

    def reset_position(self):
        self.goto(0, -self.screen_height // 2 + self.margin)