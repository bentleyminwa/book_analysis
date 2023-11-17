import pandas as pd # Import pandas library for cleaning, manipulation and analysis of data

class Loader():

    def __init__(self) -> None:
        pass

    def load_data_set(): # Loads the books dataset 
        df = pd.read_csv('data/book_data.csv', index_col = 'Title')

        return df
    
    def load_cln_data_set(): # Loads the cleaned books dataset
        df2 = pd.read_csv('data/cln_book_data.csv', index_col = 'Title')

        return df2

