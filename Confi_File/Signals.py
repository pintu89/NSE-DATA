import pandas as pd


def generate_signals(data):
    signals = pd.DataFrame(index=data.index)
    signals['Buy'] = 0
    signals['Sell'] = 0

    # Generate signals based on moving average crossover
    signals['Buy'][data['SMA_10'] > data['SMA_27']] = 1
    signals['Sell'][data['SMA_10'] < data['SMA_27']] = -1

    return signals

    if __name__ == '__main__':
        signals = generate_signals(dt5_df) # Use your own TODO:dt5_df pandas data frame in heare.

