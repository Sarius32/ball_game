from tkinter import Tk, Canvas, mainloop
import random
from ball import Ball


from consts import OFFSET, SQUARE_SIZE, HEIGHT, INTERVAL, SQUARES_PER_PLAYER, WIDTH
from square import Square
from utils import ball_out_of_bounds, get_random, intersects


class Ball_Game:
    window: Tk
    canvas: Canvas

    t = 0

    balls: list[Ball] = []

    squares: list[Square] = []

    red_remaining = 0
    red_origin = (OFFSET, OFFSET)
    red_range = ((1, 0), (0, 1))

    yellow_remaining = 0
    yellow_origin = (OFFSET + 2*SQUARES_PER_PLAYER*SQUARE_SIZE, OFFSET)
    yellow_range = ((-1, 0), (0, 1))

    blue_remaining = 0
    blue_origin = (OFFSET, OFFSET + 2*SQUARES_PER_PLAYER*SQUARE_SIZE)
    blue_range = ((1, 0), (0, -1))

    green_remaining = 0
    green_origin = (OFFSET + 2*SQUARES_PER_PLAYER*SQUARE_SIZE, OFFSET + 2*SQUARES_PER_PLAYER*SQUARE_SIZE)
    green_range = ((-1, 0), (0, -1))


    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Ball Game")
        self.window.geometry(f'{WIDTH}x{HEIGHT}')

        self.canvas = Canvas(self.window)
        self.canvas.configure(bg="black")
        self.canvas.pack(fill="both", expand=True)

        self.init_rects()

        self.animate()
        mainloop()


    def init_rects(self) -> None:
        self.squares.extend([Square((OFFSET + SQUARE_SIZE/2 + x*SQUARE_SIZE                                 , OFFSET + SQUARE_SIZE/2 + y*SQUARE_SIZE                                 ), "red", self.canvas)    for x in range(SQUARES_PER_PLAYER) for y in range (SQUARES_PER_PLAYER)])
        self.squares.extend([Square((OFFSET + SQUARE_SIZE/2 + x*SQUARE_SIZE + SQUARES_PER_PLAYER*SQUARE_SIZE, OFFSET + SQUARE_SIZE/2 + y*SQUARE_SIZE                                 ), "yellow", self.canvas) for x in range(SQUARES_PER_PLAYER) for y in range (SQUARES_PER_PLAYER)])
        self.squares.extend([Square((OFFSET + SQUARE_SIZE/2 + x*SQUARE_SIZE                                 , OFFSET + SQUARE_SIZE/2 + y*SQUARE_SIZE + SQUARES_PER_PLAYER*SQUARE_SIZE), "blue", self.canvas)   for x in range(SQUARES_PER_PLAYER) for y in range (SQUARES_PER_PLAYER)])
        self.squares.extend([Square((OFFSET + SQUARE_SIZE/2 + x*SQUARE_SIZE + SQUARES_PER_PLAYER*SQUARE_SIZE, OFFSET + SQUARE_SIZE/2 + y*SQUARE_SIZE + SQUARES_PER_PLAYER*SQUARE_SIZE), "green", self.canvas)  for x in range(SQUARES_PER_PLAYER) for y in range (SQUARES_PER_PLAYER)])


    def add_to_ball_reservoir(self) -> None:
        self.red_remaining += 1
        self.yellow_remaining += 1
        self.blue_remaining += 1
        self.green_remaining += 1


    def shoot_ball(self, origin: tuple[int, int], direction_range: tuple[tuple[int, int]], color: str) -> None:
        dir_x = random.uniform(direction_range[0][0], direction_range[1][0])
        dir_y = random.uniform(direction_range[0][1], direction_range[1][1])
        self.balls.append(Ball(origin, (dir_x, dir_y), color, self.canvas))

    def shoot_balls(self) -> None:
        if get_random(25) and self.red_remaining > 0:
            self.shoot_ball(self.red_origin, self.red_range, "red")
            self.red_remaining -= 1
        if get_random(25) and self.yellow_remaining > 0:
            self.shoot_ball(self.yellow_origin, self.yellow_range, "yellow")
            self.yellow_remaining -= 1
        if get_random(25) and self.blue_remaining > 0:
            self.shoot_ball(self.blue_origin, self.blue_range, "blue")
            self.blue_remaining -= 1
        if get_random(25) and self.green_remaining > 0:
            self.shoot_ball(self.green_origin, self.green_range, "green")
            self.green_remaining -= 1


    def animate(self) -> None:
        self.t += INTERVAL
        if self.t >= 1:
            self.t = 0
            self.add_to_ball_reservoir()

        self.shoot_balls()

        for ball in self.balls:
            if ball_out_of_bounds(ball):
                self.balls.remove(ball)
                break
            stop = False
            for square in self.squares:
                if square.color_int is not ball.color_int:
                    if intersects(ball.center, square.center):
                        square.changeColor(ball.color)
                        self.balls.remove(ball)
                        stop = True
                        break

            if not stop:
                ball.update()

        self.canvas.after(int(INTERVAL*1000), self.animate)
