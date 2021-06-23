from typing import Tuple
from lindenmayer import LindIter, turtleGraph
import numpy as np


def printMenuOptions(menuItems: np.ndarray):
    """Displays an array of menu items

    Parameters:
    ----
    menuItems: np.ndarray
        Array of menu items
    """
    for i in range(len(menuItems)):
        print(f"{i+1} - {menuItems[i]}")


def inputInt(prompt: str) -> int:
    """IO function to input an integer

    Parameters:
    ----
    prompt: str
        A string displayed to the user
    
    Returns
    ----
    integer: int
    """
    while True:
        try:
            return int(input(prompt))
        except:
            print("Please input an integer")


def inputFloat(prompt: str) -> int:
    """IO function to input a float

    Parameters:
    ----
    prompt: str
        A string displayed to the user
    
    Returns
    ----
    number: float
    """
    while True:
        try:
            return float(input(prompt))
        except:
            print("Please input a float")


def inputChars(prompt: str) -> str:
    """IO function to input a float

    Parameters:
    ----
    prompt: str
        A string displayed to the user
    
    Returns
    ----
    number: float
    """
    alphabet = "qwertyuiopåasdfghjklæøzxcvbnm"

    while True:
        userInput = input(prompt)
        if all(c.lower() in alphabet for c in userInput):
            return userInput
        print("Please input a string only containing letters from the alphabet.")


def inputBoolean(prompt: str) -> bool:
    """IO function for asking user a yes/no question

    Parameters:
    ----
    prompt: str
        A string displayed to the user
    
    Returns
    ----
    a: bool
    """
    while True:
        userRes = input(f"{prompt} [y]es / [n]o: ").lower()
        if userRes == "y" or userRes == "yes":
            return True
        elif userRes == "n" or userRes == "no":
            return False
        else:
            print("Please type [y]es or [n]o")


def displayMenu(menuItems: np.ndarray, prompt: str) -> int:
    """IO function for displaying a menu of menuItems and returns the chosen index

    Parameters:
    ----
    menuItems: np.ndarray
        List of menu items
    prompt: str
        A string displayed to the user

    Returns
    ----
    index: int
        The chosen index of menuItems
    """
    while True:
        printMenuOptions(menuItems)
        items = list(range(len(menuItems)))
        menuOptions = ", ".join([str(item + 1) for item in items])
        choice = inputInt(f"{prompt} ({menuOptions}): ") - 1
        if choice in range(len(menuItems)):
            return choice
        else:
            print(f"{choice + 1} is not a valid option")


def inputNumberOfIterations(chosenLindenmayerSystems: str,) -> Tuple[np.ndarray, int]:
    """IO function for user input of number of iterations and calculating turtleCommands. 

    Returns:
    ----
    turtleCommands: nd.array
        Turtle commands, Numpy array with altering length and angle commands [l1, a1, l2, a2..., an, ln]
        
    numberOfIterations: int
        Number of iterations the Lindermayer string has been calculated
    """

    while True:

        # IO -- input of number
        numberOfInterations = inputInt("Please choose number of iterations: ")

        # Checks
        if numberOfInterations <= 0:
            print("Please chose an positive integer")
            continue

        if numberOfInterations > 8:
            userInputIterations = inputBoolean(
                "Whoah dude, you have chosen a very large number of iterations! The program might not be able to compute the lindenmayer string or plot the output. Want to continue at your own risk?!"
            )
            if not userInputIterations:
                continue

        # Compute the lindenmayer string
        lindenmayerString = LindIter(chosenLindenmayerSystems, numberOfInterations)

        # Check if the output is larger than the max length
        if len(lindenmayerString) > 2e6:
            print(
                f"Waaaaaay to many turtlecommands! {numberOfInterations} iterations makes the Lindenmayer string exede 4 milion turtle commands!"
            )
            print("Try a smaller number of iterations :-)")
            # Jump back to the begining of the while loop
            continue

        return (turtleGraph(lindenmayerString), numberOfInterations)

