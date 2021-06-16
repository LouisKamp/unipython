
import numpy as np
from pandas.core.frame import DataFrame

#
statisticValues = ["Mean Temperature", "Mean Growth rate", "Std Temperature",
                   "Std Growth rate", "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"]


def dataStatistics(data: DataFrame, statistic: str) -> float:
    """A function to compute statistics for the data

    Keyword arguments:
    data: DataFrame -- The loaded data
    statistic: str  -- can be: "Mean Temperature", "Mean Growth rate", "Std Temperature","Std Growth rate", "Rows", "Mean Cold Growth rate", "Mean Hot Growth rate"

    Returns:
    result: float
    """
    # Mean Temperature
    if statistic == statisticValues[0]:
        result = np.mean(data["Temperature"])
    # Mean Growth rate
    if statistic == statisticValues[1]:
        result = np.mean(data["Growth rate"])
    # Std Temperature
    if statistic == statisticValues[2]:
        result = np.std(data["Temperature"])
    # Std Growth rate
    if statistic == statisticValues[3]:
        result = np.std(data["Growth rate"])
    # number of Rows
    if statistic == statisticValues[4]:
        result = len(data)
    # Mean Cold Growth rate
    if statistic == statisticValues[5]:
        index = data['Temperature'] < 20
        result = np.mean(data["Growth rate"][index])
    # Mean Hot Growth rate
    if statistic == statisticValues[6]:
        index = data['Temperature'] > 20
        result = np.mean(data["Growth rate"][index])
    return result
