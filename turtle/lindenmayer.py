#%%
import time
from typing import Dict, Literal, Tuple
import numpy as np
import math
import matplotlib.pyplot as plt

#%%

# Sets up the systems and initial strings

# Type for Lindenmayer Systems
LindemayerSystem = Tuple[Dict[str, str], str]


koch_system: Dict[str, str] = {"S": "SLSRSLS", "L": "L", "R": "R"}

koch_init = "S"

koch: LindemayerSystem = koch_system, koch_init

sierpinski_system: Dict[str, str] = {"A": "BRARB", "B": "ALBLA", "R": "R", "L": "L"}

sierpinski_init = "A"

sierpinski: LindemayerSystem = sierpinski_system, sierpinski_init


lindenmayerSystemDict: Dict[str, LindemayerSystem] = {
    "Koch": koch,
    "Sierpinski": sierpinski
}



letterValueDict = {}

def printLetterValueDict():

    if len(letterValueDict) == 0:
        print("\nNo letters are defined.\n")
    else:
        print("Letters in use:")
        for letter, value in letterValueDict.items():
            print(f"{letter} -> {value}")



#%%


def LindIter(System: Literal["Koch", "Sierpinski"], N: int) -> str:
    """Calculates the N'th number of a lindenmayer string

    Parameters
    ----
    System: Literal["Koch", "Sierpinski"]
        The name of the system the function will use to compute the lindenmayer string. Can be "Koch" or "Sierpinski"
    N: int
        The number of iterations/depth the function will calculate the lindenmayer string to.

    Raises
    ----
    ValueError
        Will raise a ValueError if the parameter system does not equal "Koch" or "Sierpinski"

    Returns
    ----
    LindenmayerString: str
        The lindenmayer string of the system to the depth of N.
    """

    # Setup the systems and initial strings

    try:
        systemDict,LindenmayerString = lindenmayerSystemDict[System]
    except KeyError:
        raise ValueError("System should either be 'Koch' or 'Sierpinski'")        

    # Calculate the LindenmayerString to the depth of N

    for i in range(N):
        LindenmayerString = "".join([systemDict[char] for char in LindenmayerString])
        if len(LindenmayerString) > 4e6:
            break

    return LindenmayerString


def turtleGraph(LindenmayerString: str) -> np.ndarray:
    """Turns a LindenmayerString into an array of graphing commands

    Parameters:
    ----
    LindenmayerString: str
        String containing a commands for a lindenmayer system for Sierpinski triangle or Koch curve

    Raises
    ----
    ValueError
        Will raise a ValueError if the program can not determine if the LindenmayerString is a Sierpinski triangle or a Koch curve

    Returns:
    ----
    turtleCommands: np.ndarray
        Numpy array with altering length and angle commands [l1, a1, l2, a2..., an, ln]
    """
    # Counts the number of lineSegments
    lineSegments = math.ceil(len(LindenmayerString)/2)

    # Counts the number of turns
    turns = math.floor(len(LindenmayerString)/2)

    # Assign commands array
    turtleCommands = np.zeros(lineSegments + turns)

    # Setsup the default linesegment length and angles
    lineSegmentLength = 0
    angleLeft = math.pi / 3
    angleRight = 0
    usingCustomSystem = False

    # Determine if the programme is looking at a Sierpinski triangle or Koch curve
    if LindenmayerString.count("A") > 0:
        # Sierpinski triangle
        lineSegmentLength = (1 / 2) ** (math.log(lineSegments) / math.log(3))
        angleRight = -math.pi * (1 / 3)
    elif LindenmayerString.count("S") > 0:
        # Koch curve
        lineSegmentLength = (1 / 3) ** (math.log(lineSegments) / math.log(4))
        angleRight = -math.pi * (2 / 3)
    elif all(c in letterValueDict for c in LindenmayerString ):
        usingCustomSystem = True
    else:
        raise ValueError("No configuration for this lindenmayer string")

    for i, letter in enumerate(LindenmayerString):
        if usingCustomSystem:
            turtleCommands[i] = letterValueDict[letter]
        elif letter == "S" or letter == "A" or letter == "B":
            turtleCommands[i] = lineSegmentLength
        elif letter == "L":
            turtleCommands[i] = angleLeft
        elif letter == "R":
            turtleCommands[i] = angleRight
        else:
            raise ValueError("No configuration for this lindenmayer string")

    return turtleCommands


def turtlePlot(turtleCommands: np.ndarray):
    """Plots turtle commands

    Parameters
    ----
    turtleCommands: np.ndarray
        Numpy array with altering length and angle commands [l1, a1, l2, a2..., an, ln]

    Returns
    ----
    None
    """

    # finds the segment commands
    segmentCommands = turtleCommands[::2]

    # finds the angle commands
    angleCommands = turtleCommands[1::2]

    # Allocates the dirrection array
    dirrectionArray = np.zeros((2, len(segmentCommands)))

    # Predefines the first vector
    dirrectionArray[:, 0] = np.array([1, 0])

    # Loops through and calculates the next vector for all angels
    for i in range(len(angleCommands)):
        dirrectionArray[:, i + 1] = np.dot(
            np.array(
                [
                    [math.cos(angleCommands[i]), -math.sin(angleCommands[i])],
                    [math.sin(angleCommands[i]), math.cos(angleCommands[i])],
                ]
            ),
            dirrectionArray[:, i],
        )

    # Allocates the coordinates array (the length needs to be one more than the number of segments)
    coordinatesArray = np.zeros((2, len(segmentCommands) + 1))

    # Defines the first coordinate as (0,0)
    coordinatesArray[:, 0] = np.array([0, 0])

    # Loops thought and calculates the next coordinate in the serries
    for i in range(len(segmentCommands)):
        coordinatesArray[:, i + 1] = (
            coordinatesArray[:, i] + segmentCommands[i] * dirrectionArray[:, i]
        )

    # Plots the coordinates
    xs, ys = coordinatesArray
    plt.plot(xs, ys, linewidth=1)
    #plt.xlim((0, 1))
    plt.show()