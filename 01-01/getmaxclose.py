import pandas as pd


def get_max_close(symbol):
    """Return the maximum closing value for stock indicated by symbol.

    Note:Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("../data/{}.csv".format(symbol))
    return df['Close'].max()


def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.

    Note:Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("../data/{}.csv".format(symbol))
    return df['Volume'].mean()


def test_run():
    for symbol in ['AAPL', 'IBM']:
        print("Max close")
        print(symbol, get_max_close(symbol))
        print("Mean volume")
        print(symbol, get_mean_volume(symbol))


if __name__ == "__main__":
    test_run()
