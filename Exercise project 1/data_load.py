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
    data = pd.read_csv(filename, names=dataColumn, delimiter=" ")
    xSize, ySize = data.shape
    truthyRows = np.ones(xSize, dtype=bool)
    for i, row in data.iterrows():
        if (row['Temperature'] >= 10 and row['Temperature'] <= 60) == False:
            truthyRows[i] = False
            print(f"The row: {i} does not have the required tempeture range!")
        if row['Growth rate'] < 0:
            truthyRows[i] = False
            print(f"The row: {i} does not have a positive growth rate!")
        if row['Bacteria'] not in bacteriaValues:
            truthyRows[i] = False
            print(f"The row: {i} contains a not allowed bacteria!")

    return data[truthyRows]
