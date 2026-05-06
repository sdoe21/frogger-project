import random
from car import Car

class CarManager:
    def __init__(self, screen_width, margin):
        self.cars = []
        self.screen_width = screen_width
        self.margin = margin

    def create_car(self):
        if random.randint(1, 6) == 1:
            y = random.randint(-250, 250)
            new_car = Car(self.screen_width, self.margin, y, 6)
            self.cars.append(new_car)

    def update(self):
        self.create_car()
        for car in self.cars:
            car.update()