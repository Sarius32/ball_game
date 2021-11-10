from random import randint

from consts import CUBE_SIZE

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

    if (distance_x > (rectangle_size/2 + ball_radius)):
        return False
    if (distance_y > (rectangle_size/2 + ball_radius)):
        return False

    if (distance_x <= (rectangle_size/2)):
        return True
    if (distance_y <= (rectangle_size/2)):
        return True

    cornerDistance_sq = (distance_x - rectangle_size/2)**2 + (distance_y - rectangle_size/2)**2

    return (cornerDistance_sq <= (ball_radius**2))