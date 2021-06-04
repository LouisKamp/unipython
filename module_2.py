

# %% Assignment 2A
import numpy as np
import math


def evaluateTaylor(x):
    y = (x-1)-(1/2)*(x-1)**2+(1/3)*(x-1)**3
    return y


# %%


a = np.array([1, 2, 3])
b = a
a[0] = 4
print(b)


# %% Exercise 2B


v1 = np.array([3, 7, 1])
v2 = np.zeros(6)
v3 = np.ones(3)
v4 = np.array([1, 2, 3, 4])
v5 = np.array([1, 2, 3, 4, 5, 10, 11, 12, 13, 14])


# %% Exercise 2C


v1 = np.array([1, 2, 3, 4, 5])
v2 = np.array([3, 4, 5, 6, 7])
v3 = np.array([1, 1, 1, 1])

np.dot(v1, v2)
v1*v2
np.sin(v1)
len(v1)
# %% Exercise 2D

v1 = np.array([4, 2, 1, 2, 5])
v2 = np.array([-1, 4, 5, -3, 6])
#v3 = v1[v1 < 3]
#v3 = v2[v2 < 0]
#v3 = v2[v2 > 0]
#v3 = v1[v1 > 100]
#v3 = v1[v1 > v2]
#v3 = v2[v2 != 5]
#v3 = v1[v1 > np.mean(v1)]

# %% Exercise 2E


v = np.array([4, 7, -2, 9, 3, -6, -4, 1])

# index = [x < 0 for x in v]
# v[index] = 0

# v*(-1)

# index = [x < np.mean(v1) for x in v]
# v[index] = 0

v1 = np.copy(v)
index = [x < 0 for x in v1]
v1[index] *= (-1)
v*v1
# v*2


# %% Assignment 2F


def computeProjection(a: np.ndarray) -> np.ndarray:
    b = np.ones(len(a))
    projection = (np.dot(a, b))/(np.dot(a, a))*a
    return projection


assert np.array_equal(computeProjection(
    np.array([2, -1])), np.array([0.4, -0.2]))
# %%


# @params boxCorners = [x1 x2 x3 x4 y1 y2 y3 y4]
# import numpy as np

def boxArea(boxCorners: np.ndarray, area: str):
    x1, x2, x3, x4, y1, y2, y3, y4 = boxCorners
    if area == "Box1":
        return (x2-x1)*(y2-y1)
    elif area == "Box2":
        return (x4-x3)*(y4-y3)
    elif area == "Intersection":
        return max(0, min(x2, x4) - max(x1, x3))*max(0, min(y2, y4)-max(y1, y3))
    elif area == "Union":
        return (x2-x1)*(y2-y1) + (x4-x3)*(y4-y3) - max(0, min(x2, x4) - max(x1, x3))*max(0, min(y2, y4)-max(y1, y3))


assert boxArea(np.array([5, 20, 14, 25, 12, 23, 5, 17]), "Intersection") == 30
# %% Optional challenge 2H


def fillSudokuRow(sudokuRow: np.ndarray):
    a = np.arange(1, 10)
    index = [x == 0 for x in sudokuRow]
    number = a[[x not in sudokuRow for x in a]][0]
    sudokuRow[index] = number
    return sudokuRow


print(fillSudokuRow(np.array([1, 2, 3, 4, 5, 6, 7, 8, 0])))

# %%
