import pandas_ta as ta

class Tech_model:        
    def SMA(self, df, low_timeperiod=10, high_timeperiod=20):
        df[f'SMA_{low_timeperiod}'] = ta.sma(df['Close'], window=low_timeperiod)
        df[f'SMA_{high_timeperiod}'] = ta.sma(df['Close'], window=high_timeperiod)
        return df[f'SMA_{low_timeperiod}'], df[f'SMA_{high_timeperiod}']

    def EMA(self, df, low_timeperiod=10, high_timeperiod=20):
        df[f'EMA_{low_timeperiod}'] = ta.ema(df['Close'], window=low_timeperiod)
        df[f'EMA_{high_timeperiod}'] = ta.ema(df['Close'], window=high_timeperiod)
        return df[f'EMA_{low_timeperiod}'], df[f'EMA_{high_timeperiod}']

    def RSI(self, df, window=14):
        df[f'RSI_{window}'] = ta.rsi(df['Close'], timeperiod=window)
        return df[f'RSI_{window}']

    def Perpus(self, df):
        if df['Close'] - df['Open'] > 1:
            return 1
        else:
            return 0
'''
sma_low = 10
sma_high = 27
ema_low = 7
ema_high = 15
period = 14
yf_dn_obj = dn.yf_dn.yf_data
dt5 = {}
for symbol in sym:
    #Technical Indicators
    tech_model = td.Tech_model()

    #SMA
    low_sma, high_sma = tech_model.SMA(df=data, low_timeperiod=sma_low, high_timeperiod=sma_high)
    
    #EMA
    low_ema, high_ema = tech_model.EMA(df=data, low_timeperiod=ema_low, high_timeperiod=ema_high)
    #RSI
    rsi = tech_model.RSI(df=data, window=period)
    #Position of Up or Down.
    data['Position'] = data.apply(tech_model.Perpus, axis=1)
'''
