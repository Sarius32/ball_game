from tkinter import Tk, Canvas, mainloop
import random
from ball import Ball


from consts import CUBE_SIZE, HEIGHT, INTERVAL, WIDTH
from square import Square
from utils import intersects


class Ball_Game:
    window: Tk
    canvas: Canvas

    t = 0

    balls: list[Ball] = []

    squares: list[Square] = []

    red_origin = (20, 20)
    red_range = ((0, 1), (1, 0))

    green_origin = (320, 320)
    green_range = ((-1.0, 0), (0, -1.0))


    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Tkinter Animation Demo")
        self.window.geometry(f'{WIDTH}x{HEIGHT}')

        self.canvas = Canvas(self.window)
        self.canvas.configure(bg="black")
        self.canvas.pack(fill="both", expand=True)

        self.init_rects()


        self.animate()
        mainloop()


    def init_rects(self):
        self.squares.extend([Square((x*CUBE_SIZE+ 20, y*CUBE_SIZE+ 20), "red", self.canvas) for x in range(10) for y in range (10)])
        self.squares.extend([Square((x*CUBE_SIZE+170, y*CUBE_SIZE+ 20), "yellow", self.canvas) for x in range(10) for y in range (10)])
        self.squares.extend([Square((x*CUBE_SIZE+ 20, y*CUBE_SIZE+170), "blue", self.canvas) for x in range(10) for y in range (10)])
        self.squares.extend([Square((x*CUBE_SIZE+170, y*CUBE_SIZE+170), "green", self.canvas) for x in range(10) for y in range (10)])


    def shoot_ball(self, origin: tuple[int, int], direction_range: tuple[tuple[int, int]], color: str):
        dir_x = random.uniform(direction_range[0][0], direction_range[1][0])
        dir_y = random.uniform(direction_range[0][1], direction_range[1][1])
        self.balls.append(Ball(origin, (dir_x, dir_y), color, self.canvas))


    def animate(self):
        self.t += INTERVAL
        if self.t >= 1:
            self.shoot_ball(self.red_origin, self.red_range, "red")
            self.shoot_ball(self.green_origin, self.green_range, "green")
            self.t = 0

        for ball in self.balls:
            stop = False
            for square in self.squares:
                if square.color is not ball.color and intersects(ball.position, square.position):
                    square.changeColor(ball.color)
                    self.balls.remove(ball)
                    stop = True
                    break

            if not stop:
                ball.update()

        self.canvas.after(int(INTERVAL*1000), self.animate)
