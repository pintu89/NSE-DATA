import Read_file as rf
from Write_dt import DataDownloader
import sys
import os
import Tech_Indi as td
sys.path.append('../Confi_file')
from Signals import *
from Chart import *
from My_Wealth import *

#Read_file
data = rf.Read_xlsx_File.Read_xlsx_File("../Data_File/sym_data/NIFTY.xlsx", int(input("0 = NFITY50\n1 = NIFTY100\n2 = NFITY200\n3 = NIFTY-NEXT50\n4 = Please inter your symbols in Port_folio1 and numbers are continues.5 6 7\n Please enter your Choice: ")))
symbols = rf.Read_xlsx_File.symbols(data)
# Wite File
file_path = "../Data_File/hisdata"
symbols = symbols[:1]
data_type = input("0:  ap_data,\n1:  balance_sheet,\n2:  historical_data,\n3:  5min_data,\nEnter data type to download: ")

# Check if data_type is specified and not empty
if data_type:
    downloader = DataDownloader(file_path, symbols=symbols)
    downloader.download_and_save_data(data_type)
else:
    print("No data type specified. Skipping download.")

Tfile = input("0: historical_data,\n1: 5min_data,\nEnter your choice: ")
if Tfile == "0":
    file_path = "../Data_File/hisdata/hdata/"
elif Tfile == "1":
    file_path = "../Data_File/hisdata/5min_data"
else:
    pass
wealth = 500
stop_loss = 50
total_profit = 0
total_loss = 0
sma_low = 10
sma_high = 100
period = 10
dt5 = {}

for symbol in symbols:
    tech_model = td.Tech_model()
    try:
        # Assuming the file names are in the format 'hisdata/symbol.xlsx'
        file = f"{file_path}/{symbol}.xlsx"
        Hdata = rf.Read_xlsx_File.Read_xlsx_File(file)
        # Do something with Hdata
        low_sma, high_sma = tech_model.SMA(df=Hdata, low_timeperiod=sma_low, high_timeperiod=sma_high)
        low_ema, high_ema = tech_model.EMA(df=Hdata, low_timeperiod=sma_low, high_timeperiod=sma_high)
        rsi = tech_model.RSI(df=Hdata, window=period)
        sig1 = Adhya_strategy(Hdata,sma_low, sma_high,period, stop_loss)

        #Hdata['Position'] = Hdata.apply(tech_model.Perpus, axis=1)
        Hdata.dropna(inplace=True)
        columns = ['Adj Close']
        dt5[symbol] = Hdata

        total_gain1, final_wealth1 = calculate_wealth(sig1, Hdata, wealth)
        profit_loss = total_gain1 - wealth
        
        if profit_loss >= 0:
            total_profit += profit_loss
            wealth = final_wealth1
            print(f"Profit for {symbol}: Rs. {profit_loss}")
        
        else:
            total_loss += abs(profit_loss)
            print(f"Total Loss for {symbol}: Rs. {abs(profit_loss)}")
            
            # Find and print details of all trades
            buy_prices = Hdata.loc[Hdata['Buy'] == 1, 'Close']
            sell_prices = Hdata.loc[Hdata['Sell'] == -1, 'Close']
            for i in range(min(len(buy_prices), len(sell_prices))):
                buy_price = buy_prices.iloc[i]
                sell_price = sell_prices.iloc[i]
                trade_profit_loss = sell_price - buy_price
                print(f"Trade {i+1}: Buy Price: Rs. {buy_price}, Sell Price: Rs. {sell_price}, Profit/Loss: Rs. {trade_profit_loss}")
        print(f"Wealth after processing {symbol}: Rs. {wealth}")
        
    except FileNotFoundError:
        pass
        #print(f"File for {symbol} not found.")


'''
        else:
            total_loss += abs(profit_loss)
            # Find buy and sell prices
            buy_prices = Hdata.loc[Hdata['Buy'] == 1, 'Close'].iloc[0]
            sell_prices = Hdata.loc[Hdata['Sell'] == -1, 'Close'].iloc[0]
            if isinstance(buy_prices, float):
                buy_prices = [buy_prices]
            if isinstance(sell_prices, float):
                sell_prices = [sell_prices]
            for i, (buy_price, sell_price) in enumerate(zip(buy_prices, sell_prices)):
                loss_amount = abs(sell_price - buy_price)
                print(f"Loss {i+1} for {symbol}: Rs. {loss_amount}, Buy Price: Rs. {buy_price}, Sell Price: Rs. {sell_price}")
        print(f"Total Amount {wealth}: Rs. {total_profit}")
        print(f"Total Loss across all symbols: Rs. {total_loss}")
        '''