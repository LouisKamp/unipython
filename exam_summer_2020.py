#%%
import numpy as np

#%%


def double_sort(X: np.ndarray):
    xSize, ySize = X.shape

    for j in range(ySize):
        indexOne = np.argsort(abs(X[:, j]))
        X[:, j] = X[:, j][indexOne]

    indexTwo = np.argsort(X[0])

    return X[:, indexTwo]


# print(double_sort(np.reshape([7, -1, 0, 5, 2, 5.2, 4, 2, 3, -2, 1, 4], [3, 4])))

#%%


def compile(program: str):
    symbols = program.split(" ")
    numbers = [int(x) for x in symbols[0::2]]
    operaters = symbols[1::2]

    result = numbers[0]

    for i, operator in enumerate(operaters):
        if operator == "A":
            result = result + numbers[i + 1]
        if operator == "S":
            result = result - numbers[i + 1]
        if operator == "M":
            result = result * numbers[i + 1]
        if operator == "D":
            result = result / numbers[i + 1]

    return result


# print(compile("2 A 3 M 4 D 8"))

#%%


def pack_clips(durations: np.ndarray, total: np.ndarray):

    totalMin, totalSeconds = total
    xShape, yShape = durations.shape

    maxDuration = totalMin * 60 + totalSeconds

    secondsPassed = 0

    for i, row in enumerate(durations):
        minRow, secRow = row
        secondsPassed += minRow * 60 + secRow
        if secondsPassed > maxDuration:
            return i
    return xShape


# print(
#     pack_clips(
#         np.reshape(
#             [
#                 3,
#                 10,
#                 4,
#                 20,
#                 0,
#                 50,
#                 1,
#                 50,
#                 10,
#                 10,
#                 1,
#                 0,
#                 3,
#                 10,
#                 4,
#                 20,
#                 0,
#                 50,
#                 1,
#                 50,
#                 10,
#                 10,
#                 1,
#                 0,
#             ],
#             [12, 2],
#         ),
#         np.array([200, 20]),
#     )
# )

#%%


def navigate(origin: str, target: str):

    kvadrantFrom = str(origin)[0]
    kvadrantTo = str(target)[0]

    navigateString = ""

    if kvadrantFrom == "1":
        if kvadrantTo == "1":
            navigateString = "H"
        if kvadrantTo == "2":
            navigateString = "W"
        if kvadrantTo == "3":
            navigateString = "SW"
        if kvadrantTo == "4":
            navigateString = "S"

    if kvadrantFrom == "2":
        if kvadrantTo == "1":
            navigateString = "E"
        if kvadrantTo == "2":
            navigateString = "H"
        if kvadrantTo == "3":
            navigateString = "S"
        if kvadrantTo == "4":
            navigateString = "SE"

    if kvadrantFrom == "3":
        if kvadrantTo == "1":
            navigateString = "NE"
        if kvadrantTo == "2":
            navigateString = "N"
        if kvadrantTo == "3":
            navigateString = "H"
        if kvadrantTo == "4":
            navigateString = "E"

    if kvadrantFrom == "4":
        if kvadrantTo == "1":
            navigateString = "N"
        if kvadrantTo == "2":
            navigateString = "NW"
        if kvadrantTo == "3":
            navigateString = "W"
        if kvadrantTo == "4":
            navigateString = "H"

    direction = f"{origin}{navigateString}{target}"
    return direction


# print(navigate(413, 202))

#%%
import math


def isPrime(number: int):
    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def isPalindromic(number: int):
    stringNumber = str(number)
    return stringNumber[-1::-1] == stringNumber


def nonpalindromic_prime(n):
    # insert your code
    numberOfNonpalindromicPrimes = 0
    number = 3
    while True:

        if isPrime(number):
            if not isPalindromic(number):
                numberOfNonpalindromicPrimes += 1
        if numberOfNonpalindromicPrimes == n:
            return number

        number += 2


print(nonpalindromic_prime(7))
