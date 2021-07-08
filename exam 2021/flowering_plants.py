from typing import List
import numpy as np


def CalcMonthBlooms(start: int, stop: int) -> List[int]:
    """Calcs months where a flower blooms
    Parames:
    ----
    start: int
        Start month
    stop: int
        Stop month

    Returns:
    ----
    months: List[int]
        List of months of a flower blooms
    """
    nStop = start
    months = [start]

    if start == 0 and stop == 0:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    while nStop != stop:
        nStop = (nStop) % 12 + 1
        months.append(nStop)

    return months


def flowering_plants(G: np.ndarray, m: int):
    # Total number of flower blooming in that month
    n = 0
    # for each flower
    for row in G:
        # If month in the months the flower blooms add one to the total
        if m in CalcMonthBlooms(row[0], row[1]):
            n += 1
    return n
