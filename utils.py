from random import randint
import math

from consts import CIRCLE_SIZE, OFFSET, SQUARE_SIZE, SQUAREROOT_TWO, SQUARES_PER_PLAYER

def random_color() -> str:
    return "#%02x%02x%02x" % (randint(0, 255), randint(0, 255), randint(0, 255))


def get_color_int(color: str) -> int:
    if color == "red":
        return 0
    if color == "green":
        return 1
    if color == "blue":
        return 2
    if color == "yellow":
        return 3
    return -1


def intersects(ball_position: tuple[float, float], rectangle_position: tuple[int, int], ball_radius: int = CIRCLE_SIZE, rectangle_size: int = SQUARE_SIZE) -> bool:
    r_max = (SQUAREROOT_TWO/2)*rectangle_size
    dist = math.hypot(ball_position[0] - rectangle_position[0], ball_position[1] - rectangle_position[1])

    if dist > ball_radius + r_max:
        return False
    
    if dist < ball_radius + r_max:
        return True

    dist_x = abs(ball_position[0] - rectangle_position[0])
    dist_y = abs(ball_position[1] - rectangle_position[1])
    if dist_x == ball_radius + rectangle_size/2 or dist_y == ball_radius + rectangle_size/2:
        return True
    return False


def ball_out_of_bounds(ball) -> bool:
    if OFFSET > ball.center[0] or OFFSET + 2*SQUARES_PER_PLAYER*SQUARE_SIZE < ball.center[0]:
        return True
    
    if OFFSET > ball.center[1] or OFFSET + 2*SQUARES_PER_PLAYER*SQUARE_SIZE < ball.center[1]:
        return True
    
    return False


def get_random(chance: int) -> bool:
    return randint(0, chance) < 1