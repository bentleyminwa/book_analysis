import pandas as pd

from load_data import Loader

# Load cleaned data for analysis
cln_data = Loader.load_cln_data_set()


print(cln_data.head())