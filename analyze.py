import pandas as pd

from load_data import Loader

# Load cleaned data for analysis
cln_data = Loader.load_cln_data_set()


# Top 10 books with highest ratings
top_10_books = cln_data.nlargest(10, 'Rating')['Rating']

print(cln_data.describe())

# Calculating the correlation between books prices and ratings
def corr_function():
    correlation = cln_data['Price'].corr(cln_data['Rating'])
    return print('\n Correlation between Book Prices and Ratings: ', correlation)

corr_function()


# Genre / Category with the highest mean rating
avg_rating_by_cat = cln_data.groupby('Category')['Rating'].mean()

# Finding the category with the highest rated mean
highest_rate_cat = avg_rating_by_cat.idxmax()
highest_avg_rating = avg_rating_by_cat.max()

print('\n Category / Genre with the highest average rating:')
print(f'{highest_rate_cat} with an average rating of {highest_avg_rating}')


# genre with the highest stock / mostly available
avb_cat = cln_data.groupby('Category')['Stock'].count()

most_avb_cat = avb_cat.idxmax()
avb_count = avb_cat.max()

print('\n Category that is most available is: ')
print(f'{most_avb_cat} with a count of {avb_count} books available')


# Average pricing of the books
avg_price = cln_data['Price'].mean()

print('\n The average price of books is: ', avg_price)