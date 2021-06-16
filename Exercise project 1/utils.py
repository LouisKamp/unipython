import os
from typing import List

from pandas.core.frame import DataFrame
from pandas.io.pytables import Term
from data_load import bacteriaTypes, bacteriaValues
import pandas as pd

import numpy as np


def inputFilepath() -> str:
    """IO function for user to input filepath

    Returns:
    filepath: str
    """
    while True:
        print("Please specify the absolute path to the datafile:")
        filepath = input(os.path.abspath(".")+"/")

        # Make sure i can load data from file
        try:
            data = pd.read_csv(filepath, delimiter=" ")
        except:
            print("Could not load file.")
            continue

        xSize, ySize = data.shape
        if ySize != 3:
            print("The file is in an incorrect format.")
            continue

        return filepath


def inputChoiceBool(choice: str) -> bool:
    """IO function for user to choose an option

    Returns:
    choice: bool
    """
    while True:
        print(choice)
        response = input("[y]es / [n]o: ").lower()
        if response == "y" or response == "yes":
            return True
        if response == "n" or response == "no":
            return False
        print("Not a valid option.")


def inputFloat(prompt: str) -> float:
    """IO function for user input a float

    Returns:
    val: float
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please input a number.")


def displayMenu(choices: List[str], prompt: str) -> int:
    """Displays a menu to the user with the a set of choices

    Keywords:
    choices: List[str] -- The list of choices the user can choose
    prompt: str        -- A prompt to the user 

    Returns:
    choice: int        --  The index the user chooses
    """
    items = list(range(len(choices)))
    itemsPrintList = ", ".join(str(x) for x in items)
    while True:
        for i, choice in enumerate(choices):
            print(f"{i} - {choice}")
        try:
            response = int(input(f"{prompt} ({itemsPrintList}): "))
            if response in range(len(choices)):
                print("")
                return response
            else:
                raise ValueError('Not valid value')
        except ValueError:
            print("Please select a valid value.\n")


# List of possible filters
filterMenuItems = ["Filter for the bacteria type",
                   "Filter for the growth rate"]


def filterMenu(data: DataFrame) -> DataFrame:
    """IO function to display the a filter menu and calcs the filter

    Returns:
    filteredData: Dataframe -- The filted data
    """
    xSize = len(data)
    filtedData = np.ones(xSize, dtype=bool)

    # Displays a menu
    userFilterResponse = displayMenu(filterMenuItems, "Choose filter")
    # Filter for the Bacteria type
    if userFilterResponse == 0:
        print("Please pick a bactera to filter")
        userTypeFilterResponse = displayMenu(bacteriaTypes, "Pick bactera")
        filtedData = data['Bacteria'] == bacteriaValues[userTypeFilterResponse]

    # Filter for the Growth rate
    if userFilterResponse == 1:
        minVal = inputFloat("Min growth rate: ")
        maxVal = inputFloat("Max growth rate: ")

        #dataColumn = ["Temperature", "Growth rate", "Bacteria"]

        filtedData = (data['Growth rate'] >= minVal) & (
            data['Growth rate'] <= maxVal)
    # Ask the user if they want to filter again
    if inputChoiceBool("Do you want to filter again?"):
        return filterMenu(data[filtedData])

    return data[filtedData]
