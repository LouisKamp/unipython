

# %% Assignment 1 Robust mean
from typing import List
import numpy as np
import math


def robust_mean(x: np.ndarray):
    mu = np.mean(x)
    sigma = math.sqrt(np.mean((x-mu)**2))
    return np.mean(x[[xi >= mu-sigma and xi <= mu+sigma for xi in x]])


print(robust_mean(np.array([5.4, 17.4, 5.5, 6.4, 4.3])))

# %% Assignment 2 Shape roundness


def shape_roundness(S: np.ndarray):
    # r = A/P

    xSize, ySize = S.shape

    def getElement(x, y):
        if (x >= 0 and x < xSize) and (y >= 0 and y < ySize):
            if S[x, y]:
                return 1
            else:
                return 0
        else:
            return 0

    P = 0

    def getSumOfNeighbors(i: int, j: int):
        return getElement(i-1, j) + getElement(i+1, j) + getElement(i, j-1) + getElement(i, j+1)

    for i in range(xSize):
        for j in range(ySize):
            if S[i][j]:
                P += 4 - getSumOfNeighbors(i, j)

    A = np.sum(S)
    return A/P


print(shape_roundness(np.array([[0, 0, 1, 1, 0, 1],
                                [0, 1, 1, 1, 1, 0],
                                [0, 1, 1, 0, 1, 0],
                                [0, 0, 0, 0, 0, 0]], dtype=np.bool)))


# %% Assignment 3 Candy exchange

def candy_exchange_v2(nCandie: int, nWrappers: int):
    if nCandie == 0 and nWrappers < 5:
        return 0

    nCandie += nWrappers//5
    nWrappers -= nWrappers//5*5

    return nCandie + candy_exchange_v2(0, nWrappers+nCandie)


def candy_exchange(n: int):
    return candy_exchange_v2(n, 0)


candy_exchange(73)
# %% Assignment 4 Change case


def change_case(v: str):
    snakeCase = "_" in v

    if snakeCase:
        x = [x.capitalize() for x in v.split("_")]
        x[0] = x[0].lower()
        return "".join(x)
    else:
        x = [l for l in v]
        for i, letter in enumerate(x):
            if letter.capitalize() == letter:
                x[i] = f"_{letter.lower()}"
        return "".join(x)

# %% Assignment 5 Nearest shop


def nearest_shop(c: int, s: List[int]):
    N = len(s)
    # If the customer’s post code exactly matches one of the shop post codes, this is the nearest shop.
    idx1 = s == c
    if len(s[idx1]) > 0:
        return s[idx1][0]

    idx2 = np.floor(s/10) == math.floor(c/10)
    if len(s[idx2]) > 0:
        return s[idx2][0]

    idx3 = np.floor(s/100) == math.floor(c/100)
    if len(s[idx3]) > 0:
        return s[idx3][0]

    idx4 = np.floor(s/1000) == math.floor(c/1000)
    if len(s[idx4]) > 0:
        return s[idx4][0]

    return s[0]


nearest_shop(3490, np.array([2300, 1890, 3990, 3590, 7900]))
# If no exact match is found, consider shops matching the customer’s post code in the first three digits. If there are 3-digit matches, the match appearing first in the list is the nearest shop.
# If no 3-digit matches are found, consider 2-digit matches in a similar manner. If no 2-digit matches are found, consider 1-digit matches.
# If no shop is matching the first digit of the customer’s post code, the shop appearing first in the list is the nearest shop.

# %%
