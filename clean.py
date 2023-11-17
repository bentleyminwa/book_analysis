import pandas as pd

from load_data import Loader

# Load the data for cleaning
data_set = Loader.load_data_set()

"""

# Explore the data set
def explore():
    display_cols = print(data_set.columns)         # returns the column names in the dataframe
    display_info = print(data_set.info())          # returns information about the column data types
    display_stats = print(data_set.describe())      # descriptive statistics about the dataframe

    return display_cols, display_info, display_stats


explore()

"""

# Dropping the rows with null values
data_set = data_set.dropna()

# Checking and Removing columns that will be of no use for analysis
