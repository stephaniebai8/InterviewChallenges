import pandas as pd
from ..Pandas import filter_by_most_traded_isin, return_isin_counts, return_trade_prices_as_list, return_df_with_volume, return_merged_frame

def test_return_types():
    assert isinstance(filter_by_most_traded_isin(), pd.DataFrame)
    assert isinstance(return_isin_counts(), pd.Series)
    assert isinstance(return_trade_prices_as_list(), list)
    assert isinstance(return_df_with_volume(), pd.DataFrame)
    assert isinstance(return_merged_frame(), pd.DataFrame)