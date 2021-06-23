from typing import Dict
from matplotlib import pyplot as plt
from utils import displayMenu, inputBoolean, inputChars, inputFloat, inputNumberOfIterations
from constants import mainMenuItems
from lindenmayer import (
    LindemayerSystem,
    lindenmayerSystemDict,
    printLetterValueDict,
    turtlePlot,
    letterValueDict,
)
import numpy as np


def main():
    print("\nHi and truly welcome to Lindenmayer system viewer 3000! Your personal Lindenmayer experience.")
    print("\nView and create your own awesome Lindenmayer systems right here, and learn awesome facts along the way.")
    print("Start by selecting a Lindenmayer system in menu (1).")
    print("More advanced users can create their own fractals in menu (3)\n")

    # Setup of vars

    chosenLindenmayerSystems = ""
    numberOfInterations = 0

    # Main loop

    while True:

        # Plot the chosen lindenmayer system

        if chosenLindenmayerSystems != "":
            print(f"\nYou have chosen the {chosenLindenmayerSystems} system with {numberOfInterations} number of iterations.\n")

        # Display main menu ("Choose Lindenmayer system", "Generate plots", "New Lindenmayer system", "Quit")
        mainMenuUserResponse = displayMenu(mainMenuItems, "Choose")


        # Choose Lindenmayer system
        if mainMenuUserResponse == 0:
            print("Please choose a system")
            # Unpacks keys of the lindenmayerSystemDict and converts their values to a numpy array
            lindenmayerSystemItems = np.array([*lindenmayerSystemDict.keys()])

            userChosenLindenmayerSystem = displayMenu(
                lindenmayerSystemItems, "Choose Lindenmayer system"
            )

            # Looks up the users chosen index in the lindenmayerSystemItems
            chosenLindenmayerSystems = lindenmayerSystemItems[
                userChosenLindenmayerSystem
            ]

            # Asks the user what number of iterations they want
            turtleCommands, numberOfInterations = inputNumberOfIterations(chosenLindenmayerSystems)

        # Generate plots
        if mainMenuUserResponse == 1:
            # Checks if the chosen lindenmayer system can be plotted by unpacking the keys of lindenmayerSystemDict
            if chosenLindenmayerSystems not in [*lindenmayerSystemDict.keys()]:
                print("Please choose a Lindenymayer system before generating plots.")
                continue

            # Setup of plot
            plt.title(
                f"{chosenLindenmayerSystems} system iteration: {numberOfInterations}"
            )
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")

            # Plot the turtleGraph of the chosen lindenmayer system
            turtlePlot(turtleCommands)

        # New Lindenmayer system
        if mainMenuUserResponse == 2:
            createNewSystemMenu()

        # Quit programme
        if mainMenuUserResponse == 3:
            print("Bye :-) Hope to see you back soon!")
            break

def createNewSystemMenu():
    print("\nYou are about to create a new Lindenmayer System.")
    print("This programme will take output of an linmayer iteration and interperate the first value as a length, the second value as an angle, the third value as a length and so on.")
    print("For a reference you can have a look at the wiki: https://en.wikipedia.org/wiki/L-system (The dragon curve is pretty cool)")
    print("Part zero: Name your new Lindenmayer system.")
    nameOfSystem = input(">")

    print("\n {nameOfSystem} - awesome name!\n")


    print("Part one: Defining global list of all the charecters you need.")


            # Print defined var/letters
    printLetterValueDict()

            # Input requeued letters for the system
    chars = input(
                "Type all the letters you want to use, without spaces or commas: "
            ).lower()


    print("Part two: define the values of all letters.")

            # Define all the values for the letters
    for char in chars:
        if char in letterValueDict:
                    # Check if letter is already defined. Makes sure the user doesent break stuff
            if not inputBoolean(f"{char} is already in use, would you like to redefine the value?"):
                continue
                # Assigns the letter to the value
        letterValueDict[char] = inputFloat(f"{char} = ")


    print("Nice! Part three: define system")

    customSystem: Dict[str, str] = {}

            # Loops though and defines the iteration rules for every letter
    for char in chars:
        while True:
            userInputForSystemChar = inputChars(f"{char} -> ").lower()
            if all(c in chars for c in userInputForSystemChar) == False:
                print("Only use letters that are defined.")
            else:
                customSystem[char] = userInputForSystemChar
                break

    printLetterValueDict()

            # Lets the user define the initial string. checks if every letter is defined

    print("Nearly done!")
    print("Part four: define the initial string.")
    initialString = ""
    while all(c not in chars for c in initialString):
        initialString = inputChars(">").lower()
        if all(c not in chars for c in initialString):
            print(
                        "Not all letters in the initial string is defined. Only use letters that are defined."
                    )

    newSystem: LindemayerSystem = customSystem, initialString
    lindenmayerSystemDict[nameOfSystem] = newSystem

    print("Congrats! You can find your new awesome Lindenmayer by choosing it in menu 1.")

if __name__ == "__main__":
    main()
