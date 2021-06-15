import os
from utils import displayMenu, filterMenu, inputFilepath

from data_load import dataLoad
from data_statistics import dataStatistics, statisticValues
from data_plot import dataPlot
import pandas as pd

import numpy as np


def main():

    # Setup

    menuItems = ["Load data", "Filter data",
                 "Display statistics", "Generate plots", "Quit"]

    data = None
    dataHasBeenLoaded = False

    # Welcome
    print("Welcome to Bacteria Data Analysis.")

    # Menu

    while True:
        userMenuResponse = displayMenu(menuItems, "Choose menu item.")
        # Load data"
        if userMenuResponse == 0:
            filepath = inputFilepath()

            print("processing data...")
            data = dataLoad(filepath)
            dataHasBeenLoaded = True
            print("processing data finished.")

        # Filter data
        if userMenuResponse == 1:
            if dataHasBeenLoaded == False:
                print("Import data before filtering.")
                continue
            data = filterMenu(data)

        # Display statistics
        if userMenuResponse == 2:
            if dataHasBeenLoaded == False:
                print("Import data before displaying statistics.")
                continue

            userTypeDisplayStatsResponse = displayMenu(
                statisticValues, "Choose")
            print(dataStatistics(
                data, statisticValues[userTypeDisplayStatsResponse]))

        # Generate plots
        if userMenuResponse == 3:
            if dataHasBeenLoaded == False:
                print("Import data before generating plots.")
                continue
            dataPlot(data)
        # Quit
        if userMenuResponse == 4:
            break


if __name__ == "__main__":
    main()
