import pandas as pd
import numpy as np

def golden_cross_strategy(data, short_window=50, long_window=200, rsi_window=14): # FIXME: This is not working.
    # Generate signals
    data['Signal'] = 0
    data.loc[data['Short_SMA'] > data['Long_SMA'], 'Signal'] = 1  # Buy signal (Golden Cross)
    data.loc[data['RSI'] > 70, 'Signal'] = -1  # Sell signal (RSI overbought)
    data.loc[data['RSI'] < 30, 'Signal'] = 1  # Buy signal (RSI oversold)
    
    return data
def Adhya_strategy(data, sma_low, sma_high, period, stop_loss): 
    # Generate signals
    data['Buy'] = 0
    data['Sell'] = 0
    buy_flag = False
    sell_flag = False
    
    for i in range(len(data)):
        if not buy_flag:
            # Check for buy position or sell position
            if data[f'RSI_{period}'].iloc[i] > 35:
                data.at[data.index[i], 'Buy'] = 1
                buy_flag = True
                sell_flag = False
                buy_price = data['Close'].iloc[i]  # Record buy price
        else:
            # Check for close buy position or sell position
            if data['Close'].iloc[i] <= buy_price * (1 - stop_loss):  # Check for stop loss
                data.at[data.index[i], 'Sell'] = -1  # Sell if stop loss is hit
                buy_flag = False
                sell_flag = True
            elif data[f'EMA_{sma_low}'].iloc[i] and \
                data[f'RSI_{period}'].iloc[i] > 70:
                data.at[data.index[i], 'Sell'] = -1
                buy_flag = False
                sell_flag = True
    
    return data

# Example usage
if __name__ == "__main__":
    # Load sample data (replace this with your actual data)
    data = pd.read_csv('sample_data.csv')  # Assuming sample_data.csv contains OHLC data
    
    # Apply the strategy
    data_with_signals = golden_cross_strategy(data)
    
    # Print the dataframe with signals
    print(data_with_signals)


