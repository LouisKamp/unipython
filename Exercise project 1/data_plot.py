# %%
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame
from constants import bacteriaTypes, bacteriaValues
import numpy as np
# %%


def dataPlot(data: DataFrame):
    """A function to plot data from a dataframe

    Keyword arguments:
    data: Dataframe -- A dataframe consiting of the columns: Temperature, Growth rate and Bacteria
    """

    fig, (ax1, ax2) = plt.subplots(2, 1)

    # Setup of the first plot

    # Filters the data
    numBacteria = [np.sum(data['Bacteria'] == x) for x in bacteriaValues]
    ax1.set_title("Number of bacteria")
    ax1.set_xlabel("Bacteria type")
    ax1.set_ylabel("Number of bacteria")
    ax1.bar(bacteriaTypes, numBacteria)

    # Setup of the secund plot
    ax2.set_title("Growth rate by temperature")
    ax2.set_xlabel("Temperature")
    ax2.set_ylabel("Growth rate")
    x = data['Temperature']
    y = data['Growth rate']
    ax2.set_xlim(10, 60)
    ax2.set_ylim(0, 1)

    # filter data for the 4 kinds of bacteria
    indexOne = data['Bacteria'] == 1
    indexTwo = data['Bacteria'] == 2
    indexThree = data['Bacteria'] == 3
    indexFour = data['Bacteria'] == 4
    # Salmonella enterica
    ax2.scatter(x[indexOne], y[indexOne])
    # Bacillus cereus
    ax2.scatter(x[indexTwo], y[indexTwo])
    # Listeria
    ax2.scatter(x[indexThree], y[indexThree])
    # Brochothrix thermosphacta
    ax2.scatter(x[indexFour], y[indexFour])
    # show all plots
    ax2.legend(bacteriaTypes)
    plt.show()
