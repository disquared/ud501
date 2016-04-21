from week1_2 import utilsreaddata as utils
import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    # Define a date range
    dates = pd.date_range('2015-01-01', '2015-12-31')

    # Choose stock symbols to read
    symbols = ['SPY']

    # Get stock data
    df = utils.get_data(symbols, dates)
    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY', fontsize=12)

    # Compute rolling mean using a 20-day window
    rm_spy = df.rolling(window=20).mean().rename(columns={'SPY': 'SPY_rolling'})
    print(df.join(rm_spy))

    # Add rolling mean to same plot
    rm_spy.plot(label='Rolling mean', ax=ax)

    # Add axis labels and legend
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend(loc='upper left')
    plt.show()


if __name__ == "__main__":
    test_run()
