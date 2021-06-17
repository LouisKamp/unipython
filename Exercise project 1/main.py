from filter import Filter, displayFilter, filterData, filterMenu
from utils import displayMenu, inputFilepath

from data_load import dataLoad
from data_statistics import dataStatistics, statisticValues
from data_plot import dataPlot
import pandas as pd
from constants import bacteriaValues, menuItems

import numpy as np


def main():

    # Setup

    data = None
    dataHasBeenLoaded = False

    baseFilter: Filter = (np.copy(bacteriaValues), (None, None))

    # Welcome
    print("Welcome to Bacteria Data Analysis.")

    # Menu

    while True:
        displayFilter(baseFilter)
        userMenuResponse = displayMenu(menuItems, "Choose menu item.")
        # Load data"
        if userMenuResponse == 0:
            filepath = inputFilepath()

            print("processing data...")
            data = dataLoad(filepath)
            dataHasBeenLoaded = True
            print("processing data finished.\n")

        # Filter data
        if userMenuResponse == 1:
            if dataHasBeenLoaded == False:
                print("Import data before filtering.")
                continue
            displayFilter(baseFilter)
            baseFilter = filterMenu(baseFilter)

        # Display statistics
        if userMenuResponse == 2:
            if dataHasBeenLoaded == False:
                print("Import data before displaying statistics.")
                continue

            displayFilter(baseFilter)
            # Displays a menu of possible stats to calculate
            userTypeDisplayStatsResponse = displayMenu(
                statisticValues, "Choose")

            # Calcs and prints the statistics the user has chosen
            print(f"{statisticValues[userTypeDisplayStatsResponse]}: ", dataStatistics(
                filterData(data, baseFilter), statisticValues[userTypeDisplayStatsResponse]))

        # Generate plots
        if userMenuResponse == 3:
            if dataHasBeenLoaded == False:
                print("Import data before generating plots.")
                continue

            print("Plotting graphs.")
            dataPlot(filterData(data, baseFilter))
        # Quit
        if userMenuResponse == 4:
            break


if __name__ == "__main__":
    main()
