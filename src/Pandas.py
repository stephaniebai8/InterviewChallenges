"""
Follow the instructions in each function's docstring. Assume all 
returned dataframes should match the schema of the input data unless
otherwise stated.

The first step of the entrypoint in this file is to print out the 
table schema as well as the first 5 lines of data. Use this to familiarize 
yourself. You can also use VSCodes built in SQLite explorer by hitting F1
and selecting 'SQLite: Open Database'. This will add the "SQLITE EXPLORER"
drawer to the left explorer bar where you can they pull up each table.

Tests are provided to validate the returned data's datatype in test_pandas.py
"""
import pandas as pd
import sqlite3

CONN = sqlite3.connect("assets/bond_data.db")
BOND_DATA = pd.read_sql("SELECT * FROM bond_marketaxess_intra_quote_table", CONN)


def filter_by_most_traded_isin() -> pd.DataFrame:
    """
    Return a pandas dataframe containing all the trades for the 
    ISIN with the most trade volume in the BOND_DATA dataframe. 
    """

    return


def isin_counts() -> pd.Series:
    """
    Return a pandas series containing the top 5 most occurring
    ISIN's and their occurrence counts
    """

    return


def trade_prices_as_list(isin: str = "US037833AK68") -> list:
    """
    Return all the prices for a given ISIN (provided as the argument/variable 'isin') as a list
    """

    return 


def df_with_volume() -> pd.DataFrame:
    """
    Return a pandas dataframe with the addition of a volume column.
    Volume can be calculated for a given row as v = Price * Quantity
    """
    
    return


def merged_frame() -> pd.DataFrame:
    """
    Return a dataframe that merges df_to_merge into BOND_DATA on Trade_Date, ISIN, and Side 
    """
    df_to_merge = pd.DataFrame({
        "Trade_Date": ["2021-10-20"] * 10,
        "ISIN": ["US037833AK68", "US126650CX62", "US92343VER15", "US61772BAB99", "US61761JVL06"] * 2,
        "Side": ["Sell", "Buy"] * 5,
        "Merged Dummy": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    })

    return
 

if __name__ == "__main__":
    print(BOND_DATA)

    print(filter_by_most_traded_isin())
    print(isin_counts())
    print(trade_prices_as_list())
    print(df_with_volume())
    print(merged_frame())
