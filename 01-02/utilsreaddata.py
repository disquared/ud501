"""Utility functions"""

import os
import pandas as pd

def symbol_to_path(symbol, base_dir="../data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')
    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col="Date",
                              parse_dates=True, usecols=['Date', 'Adj Close'])
        # rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp, how='left')  # use default how='left'
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=['SPY'])
    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2016-01-04', '2016-01-29')

    # Choose stock symbols to read
    symbols = ['AAPL']

    # Get stock data
    df = get_data(symbols, dates)
    print(df)


if __name__ == "__main__":
    test_run()
