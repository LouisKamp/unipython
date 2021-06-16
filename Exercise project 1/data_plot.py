# %%
import matplotlib.pyplot as plt
from data_load import bacteriaTypes, bacteriaValues, dataLoad
import numpy as np
# %%


def dataPlot(data):
    plotNumberOfBacteria = plt.figure(1)
    dataBacteria = np.array(data['Bacteria'])
    numBacteria = [np.sum(dataBacteria == x) for x in bacteriaValues]
    plt.title("Number of bacteria")
    plt.bar(bacteriaTypes, numBacteria)

    figGrowthRateByTemperature = plt.figure(2)
    plt.title("Growth rate by temperature")
    plt.xlabel("Temperature")
    plt.ylabel("Growth rate")
    x = data['Temperature']
    y = data['Growth rate']
    plt.xlim(10, 60)
    plt.ylim(0, 1)

    indexOne = data['Bacteria'] == 1
    indexTwo = data['Bacteria'] == 2
    indexThree = data['Bacteria'] == 3
    indexFour = data['Bacteria'] == 4
    # type one bacteria
    plt.scatter(x[indexOne], y[indexOne])

    plt.scatter(x[indexTwo], y[indexTwo])

    plt.scatter(x[indexThree], y[indexThree])

    plt.scatter(x[indexFour], y[indexFour])
    plt.legend(bacteriaTypes)

    plt.show()
