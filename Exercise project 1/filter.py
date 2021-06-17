

from typing import List, Tuple
from utils import displayMenu, inputChoiceBool, inputFloat
from pandas.core.frame import DataFrame
import numpy as np
from constants import bacteriaTypes, bacteriaValues, bacteriaValuesDict, filterMenuItems


Filter = Tuple[np.ndarray, Tuple[float, float]]


def filterData(data: DataFrame, filter: Filter):
    """Filters the data based on the filter passed to the function

    Keywords:
    data: DataFrame -- The data to be filtere
    filter: Filter  -- The filters

    """
    filterBacteriaTypes, growthRateInterval = filter
    minGrowthrate, maxGrowthrate = growthRateInterval
    # Finds the indexes that mathes all the requirements of the filter
    index = data["Bacteria"].isin(filterBacteriaTypes)

    if minGrowthrate != None and maxGrowthrate != None:
        index = index & (data["Growth rate"] >= minGrowthrate) & (
            data["Growth rate"] <= maxGrowthrate)

    return data[index]


def displayFilter(filter: Filter):
    """ Displays the filter

    Keywords:
    filter: Filter -- The filter to display
    """
    bacteriaTypes, growthRateInterval = filter
    minGrowthrate, maxGrowthrate = growthRateInterval

    filterArray: List[str] = []
    # Checks if the user has filted by bacteria type
    if len(bacteriaTypes) < 4:
        filterArray.append("filtering bacteria: " +
                           ", ".join([bacteriaValuesDict[x] for x in bacteriaTypes]))

    # Checks if the user has filted by growthrate
    if minGrowthrate != None and maxGrowthrate != None:
        minGrowthrate, maxGrowthrate = growthRateInterval
        filterArray.append(
            f"filtering min growthrate: {minGrowthrate} and max growthrate: {maxGrowthrate}")

    # If there are filters pressent, print the filter
    if len(filterArray) > 0:
        filterArray[0] = filterArray[0].capitalize()
        print(" and ".join(filterArray))
    else:
        print("No filter is pressent")


def filterMenu(oldFilter: Filter) -> Filter:
    """IO function to display the a filter menu and calcs the filter

    Returns:
    (includedBacteriaTypes: List[int], growthRateInterval: Tuple[float, float])
    """
    includedBacteriaTypes, growthRateInterval = oldFilter
    # Displays a menu
    userFilterResponse = displayMenu(filterMenuItems, "Choose filter")

    # Filter for the Bacteria type
    if userFilterResponse == 0:
        print("Please pick a bactera to filter")
        # Displays menu of all bacteria types
        userTypeFilterResponse = displayMenu(bacteriaTypes, "Pick bactera")
        # Finds the bacteria types matching users choice
        includedBacteriaTypes = bacteriaValues[bacteriaValues ==
                                               bacteriaValues[userTypeFilterResponse]]

    # Filter for the Growth rate
    if userFilterResponse == 1:
        minGrowthRate = inputFloat("Min growth rate: ")
        maxGrowthRate = inputFloat("Max growth rate: ")
        growthRateInterval = (minGrowthRate, maxGrowthRate)

    # Reset
    if userFilterResponse == 2:
        includedBacteriaTypes = np.copy(bacteriaValues)
        growthRateInterval = (None, None)

    # Ask the user if they want to filter again
    if inputChoiceBool("Do you want to filter again?"):
        return filterMenu((includedBacteriaTypes, growthRateInterval))

    return (includedBacteriaTypes, growthRateInterval)
