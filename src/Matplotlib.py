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

CONN = sqlite3.connect("assets/bond_data.db")


def graph_box_whisker_plots():
    """
    Using the top 5 results from the Pandas prompt 'filter_by_most_traded_isin', 
    plot each of the ISIN's trade prices in a box and whisker plot.
    """

    return


def graph_random_normal():
    """
    Generate a dataframe containing 1000 random integers with a normal distribution
    and graph a bar chart of them. Overlay a normal curve on the plot 
    """


    