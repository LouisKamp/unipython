# %%
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

# %%

dataColumn = ["Temperature", "Growth rate", "Bacteria"]
bacteriaValues = [1, 2, 3, 4]
bacteriaTypes = ["Salmonella enterica", "Bacillus cereus",
                 "Listeria", "Brochothrix thermosphacta"]


# %%

def dataLoad(filename: str) -> DataFrame:
    """Loads data from a space separated values file

    Keyword arguments:
    filename: str -- The name of the file to be loaded

    Returns:
    data: DataFrame
    """

    # Loads data into a dataframe
    data = pd.read_csv(filename, names=dataColumn, delimiter=" ")

    # Gets the number of rows in the dataframe
    xSize = len(data)

    # Creates a boolean array of the selected rows in the dataframe
    selectedRows = np.ones(xSize, dtype=bool)

    # Loops through the dataframe and selects the rows that compiles with the rules
    for i, row in data.iterrows():
        if (row['Temperature'] >= 10 and row['Temperature'] <= 60) == False:
            selectedRows[i] = False
            print(f"The row: {i} does not have the required tempeture range!")
        if row['Growth rate'] < 0:
            selectedRows[i] = False
            print(f"The row: {i} does not have a positive growth rate!")
        if row['Bacteria'] not in bacteriaValues:
            selectedRows[i] = False
            print(f"The row: {i} contains a not allowed bacteria!")

    # Returns the only the selected rows of the data
    return data[selectedRows]
