import pandas as pd


def generate_signals(data_dict):
    signals_dict = {}
    for symbol, data in data_dict.items():
        signals = pd.DataFrame(index=data.index)
        signals['Buy'] = 0
        signals['Sell'] = 0
        # Generate signals based on moving average crossover
        signals['Buy'][data['SMA_10'] > data['SMA_27']] = 1
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

