import pandas as pd

from load_data import Loader

# Load the data for cleaning
data_set = Loader.load_data_set()



# Explore the data set
def explore():
    display_cols = print(data_set.columns)         # returns the column names in the dataframe
    display_info = print(data_set.info())          # returns information about the column data types
    display_stats = print(data_set.describe())      # descriptive statistics about the dataframe

    return display_cols, display_info, display_stats


# explore()



# Dropping the rows with null values
data_set = data_set.dropna()

# Checking and Removing columns that will be of no use for analysis
data_set = data_set.drop(['Image', 'Description', 'UPC', 'Product Type', 'Price (incl. tax)', 'Tax', 'Number of reviews'], axis=1)

# Renaming columns
data_set.rename(columns = {'Price (excl. tax)':'Price'}, inplace = True)

# Converting the rating values to numeric data types
def convert_rating_to_numeric(rating):
    rating_mapping = {'Five':'5', 'Four':'4', 'Three':'3', 'Two':'2', 'One':'1'}
    return rating_mapping.get(rating, rating)


data_set['Rating'] = data_set['Rating'].apply(convert_rating_to_numeric)

# Convert data type to int
data_set['Rating'] = data_set['Rating'].astype('int')


# Removing unwanted characters in the price column
unwanted_chars = r'[Â£]'

data_set['Price'] = data_set['Price'].str.lstrip(unwanted_chars)

# Convert data type to float
data_set['Price'] = data_set['Price'].astype('float')
print(data_set.dtypes)