import numpy as np


def node_divergence(A: np.ndarray):

    # Find max val. Number of vertices

    maxVal = int(np.amax(A))

    # New matrix
    D = np.zeros((maxVal, 2))

    # Fill with numbers from [1 ; the maximum value]
    D[:, 0] = np.arange(1, maxVal + 1)

    # Witch rows to select then returning
    selectedRows = np.ones(maxVal, dtype=bool)

    # loop though all vertices
    for i in range(maxVal):

        # If not in matrix do nothing
        if (i + 1) not in A[:, 0] and (i + 1) not in A[:, 1]:
            selectedRows[i] = False
            continue

        # Find where the index is listed in the matrix
        indexTo = A[:, 0] == i + 1
        indexFrom = A[:, 1] == i + 1

        # Do the math
        sumTo = np.sum(A[indexTo, 2])
        sumFrom = np.sum(A[indexFrom, 2])

        D[i, 1] = sumTo - sumFrom

    # Only returns the vertices in the matrix
    return D[selectedRows]

