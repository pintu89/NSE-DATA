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
# Uses
if __name__ == '__main__':
    tech_model = Tech_model().SMA(), Tech_model().EMA(), Tech_model().RSI()
    print(tech_model.df)
    print(tech_model.df['SMA'])
    print(tech_model.df['EMA'])
    print(tech_model.df['RSI'])
'''


