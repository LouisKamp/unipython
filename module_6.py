# %%

import pandas as pd
import numpy as np

# %% Assignment 6B

import numpy as np


def computeItemCost(resourceItemMatrix: np.ndarray, resourceCost: np.ndarray):
    return np.dot(resourceItemMatrix.T, resourceCost)


print(computeItemCost(np.array([[6, 3, 0], [17, 11, 9], [4, 2, 12]]),
                      np.array([101.25, 84.00, 75.50])))

# %% Assignment 6C


def movingAvg(y: np.ndarray):
    N = y.size
    ysmooth = np.zeros(N)

    def getData(i):
        if i < 0:
            return 0
        if i > N - 1:
            return 0
        return y[i]

    for i in range(N):
        ysmooth[i] = (getData(i-2)+2*getData(i-1)+3 *
                      getData(i)+2*getData(i+1)+getData(i+2))/9

    return ysmooth

# %%


# def movingAvgV2(y: np.ndarray):
#     N = y.size
#     ys = np.zeros((1, N))
#     ysmooth = np.array([])

#     for i in range(N):
#         ysmooth = np.hstack((ys))

#     return ysmooth

# %% Assignment 6D


def letterFrequency(filename: str):
    freq = np.zeros(26)
    fileIn = open(filename, 'r')
    text = fileIn.read()
    chars = np.array([ord(char.lower()) - 97 for char in text])
    letters = chars[[char < 26 and char >= 0 for char in chars]]

    for letter in letters:
        freq[letter] += 1

    return freq/letters.size*100


print(letterFrequency('./Datafiles/small_text.txt'))


# %% Assignment 6E


def computeLanguageError(textFreq: np.ndarray):
    langFreq = np.array(pd.read_csv(
        "./letter_frequencies.csv"))[:, 1:].T
    return np.sum((textFreq-langFreq)**2, axis=1)


# %%
