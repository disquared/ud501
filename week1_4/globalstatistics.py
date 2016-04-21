from week1_2 import utilsreaddata as utils
import pandas as pd


def test_run():
    # Define a date range
    dates = pd.date_range('2015-01-01', '2015-01-31')

    # Choose stock symbols to read
    symbols = ['AAPL', 'IBM']

    # Get stock data
    df = utils.get_data(symbols, dates)
    print(df.ix['2015-01-01':'2015-01-31', symbols])
    utils.plot_data(df)

    # Compute global statistics for each stock
    print(df.mean())

if __name__ == "__main__":
    test_run()
