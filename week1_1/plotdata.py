import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    df = pd.read_csv("../data/AAPL.csv")
    print(df['Adj Close'])
    df['Adj Close'].plot()
    plt.show()


if __name__ == "__main__":
    test_run()
