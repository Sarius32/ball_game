from typing import Any
from tkinter import Tk, Canvas, mainloop

import numpy as np

class Ball:
    position: tuple[float, float]
    direction: tuple[float, float]
    radius: int

    color: str

    canvas: Canvas
    draw_obj: Any

    def __init__(self, start_position: tuple[float, float], direction: tuple[float, float], color: str, canvas: Canvas, radius: int = 5) -> None:
        self.direction = direction
        self.position = start_position
        self.radius = radius

        self.color = color

        self.canvas = canvas
        self.draw_obj = self.canvas.create_oval(self.position[0]-self.radius, self.position[1]-self.radius, self.position[0]+self.radius, self.position[1]+self.radius, fill=self.color)


    def update(self) -> None:
        self.update_position()
        self.canvas.coords(self.draw_obj, self.position[0]-self.radius, self.position[1]-self.radius, self.position[0]+self.radius, self.position[1]+self.radius)

    def update_position(self) -> None:
        self.position += self.direction / np.linalg.norm(self.direction) * 2
    
    def __del__(self) -> None:
        self.canvas.delete(self.draw_obj)