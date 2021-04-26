import math


def mean(values):
    """
    Calculates the mean of all the values in  a list.
    :param values: A list of integers
    :returns: Mean of all values
    """
    return sum(values)/len(values)


def median(values):
    """
    Calculates the median number of all the values in  a list.
    :param values: A list of integers
    :returns: Median of all values.
    """
    sorted_values = sorted(values)
    middle = math.ceil(len(sorted_values) / 2)

    # Even list length
    if len(sorted_values) % 2 == 0:
        x1 = sorted_values[middle - 1]
        x2 = sorted_values[middle]
        return (x1 + x2) / 2

    # Odd list length
    return sorted_values[middle - 1]
