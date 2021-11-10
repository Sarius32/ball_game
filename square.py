from typing import Any
from tkinter import Canvas
from consts import SQUARE_SIZE
from utils import get_color_int

class Square:
    center: tuple[int, int]
    size: int

    color: str
    color_int: int
    
    canvas: Canvas
    draw_obj: Any

    def __init__(self, center: tuple[int, int], color: str, canvas: Canvas, size: int = SQUARE_SIZE, outline: str = "grey") -> None:
        self.center = center
        self.size = size

        self.color = color
        self.color_int = get_color_int(self.color)

        self.canvas = canvas
        self.draw_obj = self.canvas.create_rectangle(self.center[0]-self.size/2, self.center[1]-self.size/2, self.center[0]+self.size/2, self.center[1]+self.size/2, fill=self.color, outline=outline)

    def changeColor(self, color: str) -> None:
        self.color = color
        self.color_int = get_color_int(self.color)
        self.canvas.itemconfig(self.draw_obj, fill=self.color)