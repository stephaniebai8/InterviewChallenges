"""
Follow the instructions in each function's docstring.

Unfortunately outputting plots in this environment is not easy. 
You will need to save the plots to disk and then open them as new
tabs in the text editor area. Instead of doing this, feel free to
write the code locally and just pasting your answers here. As a result,
only one prompt will involve the database. Generate some random dummy 
data with the same schema, and then adapt the code to work off the database.
"""
import sqlite3
import pandas as pd
import numpy as np

CONN = sqlite3.connect("assets/bond_data.db")
df = pd.read_csv("assets/bond_data.db.csv")

def graph_box_whisker_plots():
    """
    Using the top 5 results from the Pandas prompt 'filter_by_most_traded_isin', 
    plot each of the ISIN's trade prices in a box and whisker plot.
    """
    data = filter_by_most_traded_isin()
    data.loc[data.ISIN == ISIN]['PX_Bid'].plot(kind='box')
    return 


def graph_random_normal():
    """
    Generate a dataframe containing 1000 random integers with a normal distribution
    and graph a bar chart of them. Overlay a normal curve on the plot 
    """
    ##import
    import matplotlib.pyplot as plt

    ## mean and STD deviation of normal set at mean 0 and SD 1
    mu, sigma = 0, 1

    ## random distribution generation
    s = np.random.normal(mu, sigma, 1000)
    count, bins, ignored = plt.hist(s, 30, density=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu)2 / (2 * sigma2) ),
            linewidth=2, color='r')
    plt.show()
    

    