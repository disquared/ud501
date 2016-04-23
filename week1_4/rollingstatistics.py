from week1_2 import utilsreaddata as utils
import pandas as pd
import matplotlib.pyplot as plt


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    # TODO: Your code here
    # Note: Returned DataFrame must have the same number of rows
    # daily_returns = df.copy()
    # daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns = (df / df.shift(1)) - 1
    daily_returns.ix[0, ] = 0  # Pandas leaves the 0th row full of NaNs
    return daily_returns


def compute_cumulative_returns(df):
    """Compute and return the cumulative return for a given period."""
    print(df.ix[-1, ])
    print(df.ix[0, ])
    return (df.ix[-1, ] / df.ix[0, ]) - 1


def test_run():
    # Define a date range
    dates = pd.date_range('2015-01-01', '2015-1-31')

    # Choose stock symbols to read
    symbols = ['SPY']

    # Get stock data
    df = utils.get_data(symbols, dates)
    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY', fontsize=12)

    # Compute rolling mean using a 20-day window
    rm_spy = df.rolling(window=20).mean().rename(columns={'SPY': 'SPY_rolling'})
    #print(df.join(rm_spy))

    # Add rolling mean to same plot
    rm_spy.plot(label='Rolling mean', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    #plt.show()

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    utils.plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    # Compute cumulative return
    cumulative_return = compute_cumulative_returns(df)
    print(cumulative_return)


if __name__ == "__main__":
    test_run()
