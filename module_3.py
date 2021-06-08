# %% Assignment 3C

import math
import numpy as np
from typing import Dict, List

from numpy.core.defchararray import index


def acuteAngle(v1: np.ndarray, v2: np.ndarray) -> float:
    theta = math.acos(np.dot(v1, v2))
    return math.pi - theta if theta > math.pi / 2 else theta


# print(acuteAngle(np.array([-4/5, 3/5]), np.array([20/29, 21/29])))


# %% Assignment 3D

R = 6.371e6
g0 = 9.82


def gravitationalPull(x: float) -> float:
    if R <= x:
        g = g0*(R**2/x**2)
    elif 0 <= x and x <= R:
        g = (g0*x)/R
    return g


# print(gravitationalPull(1.78e6))

# %% Assignment 3E


def pH2Category(pH: float) -> str:
    category = ""

    if 0 < pH and pH < 3:
        category = "Strongly acidic"
    elif 3 <= pH and pH <= 6:
        category = "Weakly acidic"
    elif 6 < pH and pH < 8:
        category = "Neutral"
    elif 8 <= pH and pH < 11:
        category = "Weakly basic"
    elif 11 <= pH and pH < 14:
        category = "Strongly basic"
    else:
        category = "pH out of range"

    return category

# %% Optional challenge 3F


def computePassesGoalLine(point, directionVector):
    x0, y0 = point
    rx, ry = directionVector
    def y(x): return y0 + (x-x0)*(ry/rx)

    return (30.34 <= y(0) and y(0) <= 37.66 and rx < 0) or (30.34 <= y(105) and y(105) <= 37.66 and rx > 0)


# print(computePassesGoalLine(np.array([30, 20]), np.array([-10, -2])))
