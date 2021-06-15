import os
from typing import List

from pandas.core.frame import DataFrame
from pandas.io.pytables import Term
from data_load import bacteriaTypes, bacteriaValues
import pandas as pd

import numpy as np


def inputFilepath():
    while True:
        print("Please specify the absolute path to the datafile:")
        filepath = input(os.path.abspath(".")+"/")
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
    while True:
        print(choice)
        response = input("[y]es / [n]o: ").lower()
        if response == "y" or response == "yes":
            return True
        if response == "n" or response == "no":
            return False
        print("Not a valid option.")


def inputFloat(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Please input a number.")


def displayMenu(choices: List[str], prompt: str) -> int:
    items = list(range(len(choices)))
    itemsPrintList = ", ".join(str(x) for x in items)
    while True:
        for i, choice in enumerate(choices):
            print(f"{i} - {choice}")
        response = int(input(f"{prompt} ({itemsPrintList}): "))
        if response in range(len(choices)):
            return response
        print("Please select a valid value")


def filterMenu(data: DataFrame):
    xSize, ySize = data.shape
    filtedData = np.ones(xSize, dtype=bool)

    userFilterResponse = displayMenu(
        ["Filter for the bacteria type", "Filter for the growth rate"], "Choose filter")
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

        for i in range(len(data)):
            filtedData[i] = data.iloc[i,
                                      1] >= minVal and data.iloc[i, 1] <= maxVal

    if inputChoiceBool("Do you want to filter again?"):
        return filterMenu(data[filtedData])

    return data[filtedData]
