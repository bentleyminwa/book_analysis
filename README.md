# Book_analysis

This is a python pandas project for a Trending Books Dataset obtained from Kaggle


### Loading data

Using the Loader class, the required dataset is loaded for analysis. Code for this function is located in the load_data.py file

### Explore data

Created a new file called clean.py. This will primarily be used for exploring, cleaning and manipulation of the data. But first, we explore the data set.

### Cleaning data

#### Checking for and Removing Duplicate data

This was the first step of cleaning the dataset. Checked for the number of duplicate data that might be in the dataframe. There was none!

#### Checking for null values

The second step was to check for null values. There were only two null values in the description column, so getting rid of those rows was the next course of action.

#### Check and Remove columns that will of no use to our analysis

The columns to be dropped that were essentially of no use to our analysis were:
- "Image"
- "Description"
- "UPC"
- "Product Type"
- "Price (incl. tax)"
- "Tax" - Tax on every book was 0 
- "Number of reviews" - Every review was 0

#### Renaming columns

Some columns that remained were not properly named.

#### Converting data types

columns like rating and price had been assigned wrong data types(object). They had to be converted to int and float respectively

### Writing file to csv

The cleaned dataset is wrote to the data directory for analysis

### Load cleaned data set

The cleaned data set is loaded into the analyze.py file ready for analysis and visualization

### Analysis

Meaningful insights that could be drawn such a dataset are:

- Books with highest ratings
- Category/Genre that is most available
- Correlation between Pricing and Ratings
- Genre with the highest rating
- Average pricing of the books

#### Correlation between Price and Rating

Value obtained for correlation was 0.03014

Correlation values ranges from -1 to 1:
- 1 indicates a perfect positive correlation
- 0 indicates no correlation
- -1 indicates a perfect negative correlation

Analysis indicates there to be a positive correlation between Price and Rating