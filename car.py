import turtle

class Car(turtle.Turtle):
    def __init__(self, screen_width, margin, y, speed):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color("red")

        self.screen_width = screen_width
        self.margin = margin
        self.speed_val = speed

        self.goto(screen_width // 2 + margin, y)

    def update(self):
        self.backward(self.speed_val)

        if self.xcor() < -self.screen_width // 2 - self.margin:
            self.goto(self.screen_width // 2 + self.margin, self.ycor())