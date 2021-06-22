import math
from utils import displayMenu, inputBoolean, inputInt
from constants import mainMenuItems
from lindenmayer import LindIter, lindenmayerSystemDict, turtleGraph, turtlePlot
import numpy as np
import time


def inputNumberOfIterations():
    while True:
        numberOfInterations = inputInt("Please choose number of iterations: ")

        if numberOfInterations <= 0:
            print("Please chose an positive integer")
            continue

        if numberOfInterations > 11:
            print(
                "You have chosen a very large number of iterations, please choose a value under 12"
            )
            continue

        if numberOfInterations > 8:
            userInputIterations = inputBoolean(
                "You have chosen a very large number of iterations. This might take a very long time to compute, are you sure you want to continue?"
            )
            if not userInputIterations:
                continue

        return numberOfInterations


def main():
    print("Welcome to Lindenmayer system")

    chosenLindenmayerSystems = ""
    numberOfInterations = 0

    while True:
        mainMenuUserResponse = displayMenu(mainMenuItems, "Choose")

        # Choose Lindenmayer system
        if mainMenuUserResponse == 0:
            print("Please choose a system")
            lindenmayerSystemItems = np.array([*lindenmayerSystemDict.keys()])

            chosenLindenmayerSystems = lindenmayerSystemItems[
                displayMenu(lindenmayerSystemItems, "Choose Lindenmayer system")
            ]
            numberOfInterations = inputNumberOfIterations()

        if mainMenuUserResponse == 1:
            if chosenLindenmayerSystems not in [*lindenmayerSystemDict.keys()]:
                print("Please choose a Lindenmayer system before generating plots")
                continue

            turtlePlot(
                turtleGraph(LindIter(chosenLindenmayerSystems, numberOfInterations))
            )
        if mainMenuUserResponse == 2:
            break


if __name__ == "__main__":
    main()
