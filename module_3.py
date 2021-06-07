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

# %% Assignment 4D


def fermentationRate(measuredRate: np.ndarray, lowerBound: float, upperBound: float):
    index = [x > lowerBound and x < upperBound for x in measuredRate]
    return np.mean(measuredRate[index])


# print(fermentationRate(
#    np.array([20.1, 19.3, 1.1, 18.2, 19.7, 121.1, 20.3, 20.0]), 15, 25))

# %% Assignment 4E


def bacteriaGrowth(n0: float, alpha: float, K: float, N: float):
    nt = n0
    tN = 0
    while nt < N:
        nt = (1+alpha*(1-nt/K))*nt
        tN += 1
    return tN


# print(bacteriaGrowth(100.0, 0.4, 1000.0, 500.0))

# %% Assignment 4F


def removeIncomplete(ids):

    idComplete = []

    for id in ids:
        num = math.floor(id)
        if (num + 0.1 in ids) and (num + 0.2 in ids) and (num + 0.3 in ids):
            idComplete.append(id)

    return idComplete


# print(removeIncomplete(
#    np.array([1.1, 1.3, 2.1, 2.2, 3.1, 3.3, 4.1, 4.2, 4.3])))


# %% Optional challenge 4G


def clusterStep(originalArr: np.ndarray, arrOne: np.ndarray, arrTwo: np.ndarray):

    meanOne = np.mean(arrOne)
    meanTwo = np.mean(arrTwo)

    allocateArrOne = np.zeros(originalArr.size, dtype=np.bool)
    allocateArrTwo = np.zeros(originalArr.size, dtype=np.bool)

    for i in range(originalArr.size):
        allocateArrOne[i] = abs(meanTwo - originalArr[i]
                                ) >= abs(meanOne - originalArr[i])
        allocateArrTwo[i] = abs(meanTwo - originalArr[i]
                                ) < abs(meanOne - originalArr[i])

    newArrOne = originalArr[allocateArrOne]
    newArrTwo = originalArr[allocateArrTwo]

    if np.array_equal(arrOne, newArrOne) and np.array_equal(arrTwo, newArrTwo):
        resArr = np.ones(originalArr.size)
        resArr[allocateArrTwo] = 2
        return resArr
    else:
        return clusterStep(originalArr, newArrOne, newArrTwo)


def clusterAnalysis(reflectance: np.ndarray):
    indexOne = [x % 2 == 0 for x in np.arange(reflectance.size)]
    indexTwo = [x % 2 != 0 for x in np.arange(reflectance.size)]

    return clusterStep(reflectance, reflectance[indexOne], reflectance[indexTwo])


print(clusterAnalysis(
    np.array([10.0, 12.0, 10.0, 12.0, 9.0, 11.0, 11.0, 13.0])))
