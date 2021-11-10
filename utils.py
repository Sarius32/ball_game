from random import randint

from consts import CUBE_SIZE

def random_color() -> str:
    return "#%02x%02x%02x" % (randint(0, 255), randint(0, 255), randint(0, 255))


def intersects(ball_position: tuple[float, float], rectangle_position: tuple[int, int], ball_radius: int = 5, rectangle_size: int = CUBE_SIZE) -> bool:
    distance_x = abs(ball_position[0] - rectangle_position[0])
    distance_y = abs(ball_position[1] - rectangle_position[1])

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