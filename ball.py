from typing import Any
from tkinter import Tk, Canvas, mainloop

import numpy as np
from consts import BALL_SPEED, CIRCLE_SIZE
from utils import get_color_int

class Ball:
    
    center: tuple[float, float]
    direction: tuple[float, float]
    radius: int

    color: str
    color_int: int

    canvas: Canvas
    draw_obj: Any

    def __init__(self, center: tuple[float, float], direction: tuple[float, float], color: str, canvas: Canvas, radius: int = CIRCLE_SIZE) -> None:
        self.direction = direction
        self.center = center
        self.radius = radius

        self.color = color
        self.color_int = get_color_int(self.color)

        self.canvas = canvas
        self.draw_obj = self.canvas.create_oval(self.center[0]-self.radius, self.center[1]-self.radius, self.center[0]+self.radius, self.center[1]+self.radius, fill=self.color)


    def update(self) -> None:
        self.update_position()
        self.redraw()
        
    def update_position(self) -> None:
        self.center += self.direction / np.linalg.norm(self.direction) * BALL_SPEED
    def redraw(self) -> None:
        self.canvas.coords(self.draw_obj, self.center[0]-self.radius, self.center[1]-self.radius, self.center[0]+self.radius, self.center[1]+self.radius)

    
    def __del__(self) -> None:
        self.canvas.delete(self.draw_obj)