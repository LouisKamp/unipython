# %%
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from data_load import bacteriaTypes, bacteriaValues, dataLoad
import numpy as np
# %%


def dataPlot(data: DataFrame):
    """A function to plot data from a dataframe

    Keyword arguments:
    data: Dataframe -- A dataframe consiting of the columns: Temperature, Growth rate and Bacteria
    """

    # Setup of the first plot
    plotNumberOfBacteria = plt.figure(1)

    # Filters the data
    dataBacteria = np.array(data['Bacteria'])
    numBacteria = [np.sum(dataBacteria == x) for x in bacteriaValues]
    plt.title("Number of bacteria")
    plt.bar(bacteriaTypes, numBacteria)

    # Setup of the secund plot
    figGrowthRateByTemperature = plt.figure(2)
    plt.title("Growth rate by temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    x = data['Temperature']
    y = data['Growth rate']
    plt.legend(bacteriaTypes)
    plt.xlim(10, 60)
    plt.ylim(0, 1)

    # filter data for the 4 kinds of bacteria
    indexOne = data['Bacteria'] == 1
    indexTwo = data['Bacteria'] == 2
    indexThree = data['Bacteria'] == 3
    indexFour = data['Bacteria'] == 4
    # Salmonella enterica
    plt.scatter(x[indexOne], y[indexOne])
    # Bacillus cereus
    plt.scatter(x[indexTwo], y[indexTwo])
    # Listeria
    plt.scatter(x[indexThree], y[indexThree])
    # Brochothrix thermosphacta
    plt.scatter(x[indexFour], y[indexFour])
    # show all plots
    plt.show()
