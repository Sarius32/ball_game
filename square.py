from typing import Any
from tkinter import Canvas
from consts import CUBE_SIZE

class Square:
    position: tuple[int, int]
    size: int

    color: str
    
    canvas: Canvas
    draw_obj: Any

    def __init__(self, position: tuple[int, int], color: str, canvas: Canvas, size: int = CUBE_SIZE, outline: str = "grey") -> None:
        self.position = position
        self.size = size

        self.color = color

        self.canvas = canvas
        self.draw_obj = self.canvas.create_rectangle(self.position[0], self.position[1], self.position[0]+self.size, self.position[1]+self.size, fill=self.color, outline=outline)

    def changeColor(self, color: str) -> None:
        self.color = color
        self.canvas.itemconfig(self.draw_obj, fill=self.color)