# %% Assignment 4D

import numpy as np


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

# %%
