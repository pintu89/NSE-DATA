import matplotlib.pyplot as plt

def plot_signals(dataframe, symbol, period, Gain):
    # Plotting the Close price
    plt.figure(figsize=(12, 6))
    plt.plot(dataframe[symbol].index, dataframe[symbol]['Close'], label='Close Price', color='blue')
    # Plotting the RSI
    plt.plot(dataframe[symbol].index, dataframe[symbol][f'RSI_{period}'], label='RSI', color='black')

    # Plotting Buy signals
    plt.plot(dataframe[symbol][dataframe[symbol]['Buy'] == 1].index,
             dataframe[symbol]['Close'][dataframe[symbol]['Buy'] == 1],
             '^', markersize=3, color='green', lw=0, label='Buy Signal')

    # Plotting Sell signals
    plt.plot(dataframe[symbol][dataframe[symbol]['Sell'] == -1].index,
             dataframe[symbol]['Close'][dataframe[symbol]['Sell'] == -1],
             'v', markersize=3, color='red', lw=0, label='Sell Signal')

    plt.title(Gain)
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.show()

def plot_Loss_signals(data, symbol, period, Gain):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label='Close Price')
    
    # Plot buy signals
    plt.plot(data[data['Buy'] == 1].index, 
             data['Close'][data['Buy'] == 1], 
             '^', markersize=10, color='g', lw=0, label='Buy Signal')
    
    # Plot sell signals
    plt.plot(data[data['Sell'] == -1].index, 
             data['Close'][data['Sell'] == -1], 
             'v', markersize=10, color='r', lw=0, label='Sell Signal')
    
    # Add title and legend
    plt.title(f"{symbol}: {Gain}")
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.show()


# Example usage:
# plot_signals(dt5, 'AAPL')  # Assuming 'dt5' is your dataframe and 'AAPL' is the symbol
