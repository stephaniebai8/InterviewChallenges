"""
Follow the instructions in each function's docstring.

Where relevant, attempt to do all querying/filtering/manipulation
within your SQL statements as opposed to doing so with 
dataframe operations. If you do get stumped on SQL specifics, 
attempt to return the correct information via pandas operations. 

There is an example query bellow meant to show the easiest means
of querying the database and getting the output as a dataframe.
"""
from datetime import datetime, date
import pandas as pd
import sqlite3

CONN = sqlite3.connect("assets/bond_data.db")


def bond_data_between_timestamps(
    isin: str = "US037833AK68", 
    date_start: date = datetime(2022, 2, 1), 
    date_stop: datetime = datetime(2022, 2, 5), 
    columns=[]
) -> pd.DataFrame:
    """
    Query the database for all rows where the ISIN is equal to provided ISIN,
    and Trade_Date is between the provided date_start and date_stop variables.
    Return a dataframe containing the resultant data with only the columns 
    provided in the columns variable. The only dataframe operation should be
    trimming the columns. All query filtering should be done in SQL

    Use the database table 'bond_intra_composite_price_table'
    """

    return


def closest_previous_timestamp_matches(
    isins: list[str] = ["USP68788AA97", "USP06518AH06", "USP3579ECJ49", "USP90603AN40", "US716564AB55"], 
    timestamp: datetime = datetime(2022, 2, 3, 12, 0, 0, 0)
) -> pd.DataFrame:
    """
    Given a list of ISINs and a timestamp, return a dataframe containing 
    one row for each ISIN in the list where the Last_Update column is the
    closest PREVIOUS timestamp

    Use the database table 'bond_intra_composite_price_table'
    """

    return


def summary():
    """
    Return general summary statistics you think would be important 
    for the table. This is intentionally open-ended.

    Use the database table 'bond_marketaxess_intra_quote_table'
    """

    return


if __name__ == "__main__":
    ################################################### Querying Example: 
    example_data = pd.read_sql(
        """
        SELECT * 
        FROM bond_marketaxess_intra_quote_table
        WHERE Trade_Date > "2023-01-01"
        """,
        CONN
    )
    print(example_data.head())
    ###################################################

    print(bond_data_between_timestamps())
    print(closest_previous_timestamp_matches())
    print(summary())
