#%%

from typing import Dict, List, Literal
import numpy as np


#%%


def fit_windows(b: np.ndarray, w: np.ndarray, side: Literal["length", "width", "all"]):
    length, width, height = b
    windowWidth, windowHeight = w

    if side == "length":
        c = 2 * (length // windowWidth) * (height // windowHeight)
    if side == "width":
        c = 2 * (width // windowWidth) * (height // windowHeight)
    if side == "all":
        c = 2 * (length // windowWidth) * (height // windowHeight) + 2 * (
            width // windowWidth
        ) * (height // windowHeight)
    return c


# print(fit_windows(np.array([37, 20, 10]), np.array([1.1, 1.75]), "length"))

#%%


def count_novel(text: str):

    words: List[str] = text.lower().split(" ")
    novelWords: List[str] = []
    c: List[int] = []

    for word in words:
        if word not in novelWords:
            novelWords.append(word)
        c.append(len(novelWords))

    return np.array(c)


# print(count_novel("the man and another man walked down the street"))

# %%


def count_peaks(A):
    # insert your code

    xSize, ySize = A.shape

    def isANeighbor(x, y):
        if (x >= 0 and x < xSize) and (y >= 0 and y < ySize):
            return True
        return False

    def getNeighbors(x, y):
        neighbors = []
        if isANeighbor(x - 1, y):
            neighbors.append(A[x - 1, y])

        if isANeighbor(x + 1, y):
            neighbors.append(A[x + 1, y])

        if isANeighbor(x, y - 1):
            neighbors.append(A[x, y - 1])

        if isANeighbor(x, y + 1):
            neighbors.append(A[x, y + 1])

        return neighbors

    c = 0

    for i in range(xSize):
        for j in range(ySize):
            if any(A[i, j] >= x + 2 for x in getNeighbors(i, j)):
                c += 1

    return c


# print(count_peaks(np.reshape([1, 2, 3, 5, 3, 7, 7.1, 3, 3, 3, 4, 4, 7, 7.3], [2, 7])))
# %%


def classify_flower(D, q):
    index = q != 0

    A = D[:, index]

    B = A[:, :-1] == q[index][:-1]

    (indices,) = np.where([(x == True).all() for x in B])

    sorted_indices = np.argsort(np.abs(D[indices, -1] - q[-1]))

    # The rows are indexed from one
    s = indices[sorted_indices] + 1
    return s


# print(
#     classify_flower(
#         np.reshape(
#             [4, 1, 2, 3, 10.1, 4, 1, 2, 2, 20.5, 4, 2, 3, 3, 25.7, 5, 2, 3, 1, 19.4],
#             [4, 5],
#         ),
#         np.array([4, 0, 0, 3, 21.1]),
#     )
# )

#%%


def qualify(A: np.ndarray, R: np.ndarray):
    points = np.zeros(4)

    xSize, ySize = A.shape

    for i in range(xSize):
        if R[i][0] == R[i][1]:
            points[A[i][0] - 1] += 1
            points[A[i][1] - 1] += 1

        if R[i][0] > R[i][1]:
            points[A[i][0] - 1] += 3

        if R[i][0] < R[i][1]:
            points[A[i][1] - 1] += 3

    return np.argsort(points)[::-1][0:2] + 1


print(
    qualify(
        np.reshape([1, 2, 3, 4, 2, 4, 1, 3, 1, 4, 2, 3], [6, 2]),
        np.reshape([1, 1, 0, 0, 0, 0, 1, 0, 2, 1, 1, 2], [6, 2]),
    )
)
# %%
