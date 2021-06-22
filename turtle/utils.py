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
    """IO function to input a integer

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


def inputBoolean(prompt: str):
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

