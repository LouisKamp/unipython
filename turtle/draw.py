import turtle
from typing import Dict, List, Tuple, Union
import math

koch_system: Dict[str, str] = {
    "S": "SLSRSLS",
    "L": "L",
    "R": "R"
}

koch_init = "S"

sierpinski_system: Dict[str, str] = {
    "A": "BRARB",
    "B": "ALBLA",
    "R": "R",
    "L": "L"
}

sierpinski_init = "A"


def lind_iter(system: Dict[str, str], lind_start_string: str, N: int) -> str:
    lind_string = lind_start_string
    for i in range(N):
        lind_string = "".join([system[char]
                               for char in lind_string])

    return lind_string


def turtle_graph(lind_string: str, N: int) -> List[Union[float]]:
    screen = turtle.Screen()
    screen.setup(width=1000, height=1000, startx=0, starty=0)
    #screen.setworldcoordinates(-1000, -1000, 1000, 1000)
    l = (2000/(3**N))
    turtle.radians()
    turtle.screensize(1, 1)
    turtle.speed(0)
    turtle.hideturtle()

    for c in lind_string:
        if c == "S" or "A" or "B":
            turtle.forward(l)
        if c == "R":
            # turtle.right(2*math.pi/3)
            turtle.right(math.pi/3)
        if c == "L":
            turtle.left(math.pi/3)
    turtle.done()


N = 8

turtle_graph(lind_iter(sierpinski_system, sierpinski_init, N), N)

# turtle.forward(100)
# turtle.left((180/math.pi)*math.pi/3)
# turtle.forward(100)
# turtle.done()
