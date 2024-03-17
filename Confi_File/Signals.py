import pandas as pd
import numpy as np

# This code is not working.
def generate_signals(data_dict,symbol,sma_low,sma_high):
    signals_dict = {}
    for symbol, data in data_dict.items():
        signals = pd.DataFrame(index=data.index)
        signals['Buy'] = 0
        signals['Sell'] = 0
        # Generate signals based on moving average crossover
        signals['Buy'][data(f"[{symbol}][[{sma_low}]]"), > (f"[{symbol}][[{sma_high}]]") = 1
        signals['Sell'][data['SMA_10'] < data['SMA_27']] = -1
        signals_dict[symbol] = signals
    return signals_dict

if __name__ == '__main__':
    # Generate signals for the current symbol
    signals = generate_signals(dt5)

    # Display the signals for the current symbol
    for symbol, signals_df in signals.items():
        print(f"Signals for symbol {symbol}:")
        print(signals_df) # Use your own TODO:dt5_df pandas data frame in heare.

def golden_cross_strategy(data, short_window=50, long_window=200, rsi_window=14):
    # Generate signals
    data['Signal'] = 0
    data.loc[data['Short_SMA'] > data['Long_SMA'], 'Signal'] = 1  # Buy signal (Golden Cross)
    data.loc[data['RSI'] > 70, 'Signal'] = -1  # Sell signal (RSI overbought)
    data.loc[data['RSI'] < 30, 'Signal'] = 1  # Buy signal (RSI oversold)
    
    return data

# Example usage
if __name__ == "__main__":
    # Load sample data (replace this with your actual data)
    data = pd.read_csv('sample_data.csv')  # Assuming sample_data.csv contains OHLC data
    
    # Apply the strategy
    data_with_signals = golden_cross_strategy(data)
    
    # Print the dataframe with signals
    print(data_with_signals)


