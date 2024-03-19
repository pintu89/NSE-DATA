def calculate_wealth(signals, data, wealth):
    # Initialize buy and sell variables
    buy_price = None
    sell_price = None
    in_position = False  # Flag to track if currently in a position (buy)

    # Initialize variables for tracking total gain and number of trades
    total_gain = 0
    num_trades = 0

    # Iterate through signals
    for index, row in signals.iterrows():
        if row['Buy'] == 1 and not in_position:  # Buy signal and not in a position
            if 'Close' in data:  # Check if 'Close' column exists
                buy_price = data.loc[index, 'Close']
                in_position = True  # Set flag to true
        elif row['Sell'] == -1 and in_position:  # Sell signal and in a position
            if 'Close' in data:  # Check if 'Close' column exists
                sell_price = data.loc[index, 'Close']
                gain = (sell_price - buy_price)  # Calculate gain
                total_gain += gain
                num_trades += 1
                # Reset buy and sell prices and position flag
                buy_price = None
                sell_price = None
                in_position = False  # Set flag to false

    # Calculate final wealth
    final_wealth = wealth + total_gain

    # Return total gain and final wealth
    return total_gain, final_wealth
