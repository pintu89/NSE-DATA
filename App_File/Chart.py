import matplotlib.pyplot as plt

def plot_signals(dataframe, symbol):
    # Plotting the Close price
    plt.figure(figsize=(12, 6))
    plt.plot(dataframe[symbol].index, dataframe[symbol]['Close'], label='Close Price', color='blue')

    # Plotting Buy signals
    plt.plot(dataframe[symbol][dataframe[symbol]['Buy'] == 1].index,
             dataframe[symbol]['Close'][dataframe[symbol]['Buy'] == 1],
             '^', markersize=10, color='green', lw=0, label='Buy Signal')

    # Plotting Sell signals
    plt.plot(dataframe[symbol][dataframe[symbol]['Sell'] == -1].index,
             dataframe[symbol]['Close'][dataframe[symbol]['Sell'] == -1],
             'v', markersize=10, color='red', lw=0, label='Sell Signal')

if __name__ == '__main__':
    plt.title('Golden Cross and RSI Strategy Signals')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.show()

# Example usage:
# plot_signals(dt5, 'AAPL')  # Assuming 'dt5' is your dataframe and 'AAPL' is the symbol
