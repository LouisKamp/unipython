import numpy as np


dataColumn = ["Temperature", "Growth rate", "Bacteria"]
bacteriaValues = np.array([1, 2, 3, 4])
bacteriaTypes = ["Salmonella enterica", "Bacillus cereus",
                 "Listeria", "Brochothrix thermosphacta"]
bacteriaValuesDict = {
    1: "Salmonella enterica",
    2: "Bacillus cereus",
    3: "Listeria",
    4: "Brochothrix thermosphacta"
}
# List of possible filters
filterMenuItems = ["Filter for the bacteria type",
                   "Filter for the growth rate", "Reset filter"]
menuItems = ["Load data", "Filter data",
             "Display statistics", "Generate plots", "Quit"]
