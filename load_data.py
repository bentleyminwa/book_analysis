import os
import pandas as pd # Import pandas library for cleaning, manipulation and analysis of data

class Loader():

    def __init__(self) -> None:
        pass

    def load_data_set(): # Loads the books dataset 
        relative_path = 'data/book_data.csv'
        absolute_path = os.path.join(os.getcwd(), relative_path)

        df = pd.read_csv(absolute_path)

        return df


data_set = Loader.load_data_set()
print(data_set.columns)