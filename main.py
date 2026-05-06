import turtle
from player import Player
from car_manager import CarManager

# Config
SCREEN_W, SCREEN_H = 900, 600
PLAYER_MARGIN = 30
CAR_MARGIN = 20
STEP = 20
TICK_MS = 40
COLLISION_DIST = 20

# Setup screen
screen = turtle.Screen()
screen.setup(SCREEN_W, SCREEN_H)
screen.title("Frogger")
screen.tracer(0)

# Create objects
player = Player(SCREEN_H, PLAYER_MARGIN, STEP)
car_manager = CarManager(SCREEN_W, CAR_MARGIN)

# Controls
screen.listen()
screen.onkeypress(player.move_up, "Up")

def game_update():
    # Move cars
    car_manager.update()

    # Collision detection
    for car in car_manager.cars:
        if player.distance(car) < COLLISION_DIST:
            player.reset_position()

    # Goal reached
    if player.ycor() > SCREEN_H // 2 - PLAYER_MARGIN:
        player.reset_position()
        print("Level up!")

    screen.update()
    screen.ontimer(game_update, TICK_MS)

# Start game
game_update()
screen.mainloop()