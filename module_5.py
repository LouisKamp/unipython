
# %%


import random
import math
import numpy as np

# %% Assignment 5A


def convertTemperature(T: float, unitFrom: str, unitTo: str) -> float:
    """Convert between temperatures

    Keyword arguments:
    T: float      -- temperature in Kelvin(K), Celsius(C) or Fahrenheit(F)

    unitFrom: str -- "Celsius", "Fahrenheit", or "Kelvin"

    unitTo: str   -- "Celsius", "Fahrenheit", or "Kelvin"

    """

    if unitFrom == "Celsius":
        if unitTo == "Fahrenheit":
            return 1.8*T+32
        if unitTo == "Kelvin":
            return T+273.3

    if unitFrom == "Fahrenheit":
        if unitTo == "Celsius":
            return (T-32)/1.8
        if unitTo == "Kelvin":
            return (T+459.67)/1.8

    if unitFrom == "Kelvin":
        if unitTo == "Celsius":
            return T - 273.15
        if unitTo == "Fahrenheit":
            return 1.8*T-459.67

    return T


print(convertTemperature(50.0, "Fahrenheit", "Celsius"))

# %% Assignment 5E


def circleAreaMC(xvals: np.ndarray, yvals: np.ndarray):

    numberOfPointsInsideTheCircle = 0
    for i in range(xvals.size):
        if math.sqrt(xvals[i]**2 + yvals[i]**2) <= 1:
            numberOfPointsInsideTheCircle += 1

    return 4*numberOfPointsInsideTheCircle/xvals.size


print(circleAreaMC(np.array([-0.1, 0.7, 0.8, 0.5, -0.4]),
                   np.array([0.3, -0.1, 0.9, 0.6, -0.3])))

# %% Optional challenge 5F


def thermoEquilibrium(N, r: np.ndarray):

    rightN = 0
    leftN = N

    time = 0

    def probabilityLeftToRight(Nl): return Nl/N
    #def probabilityRightToLeft(Nl): return 1 - probabilityLeftToRight(Nl)

    for rand in r:
        if leftN != rightN:
            if rand <= probabilityLeftToRight(leftN):
                leftN -= 1
                rightN += 1
            else:
                leftN += 1
                rightN -= 1
            time += 1
        else:
            return time
    return 0


print(thermoEquilibrium(50.0, np.array([0.16, 0.04, 0.72, 0.09, 0.17, 0.60, 0.26,
                                        0.65, 0.69, 0.74, 0.45, 0.61, 0.23, 0.37, 0.15, 0.83, 0.61, 1.00, 0.08, 0.44])))

# %%
