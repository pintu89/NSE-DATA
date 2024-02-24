import pandas_ta as ta

class Tech_model:
    def __init__(self):
        self.df = df
        self.df['Adj Close'] = self.df['Adj Close'].astype(float)
        

    def SMA(self):
        self.df['SMA'] = ta.SMA(self.df['Adj Close'], timeperiod=10)
        return self.df['SMA']

    def EMA(self):
        self.df['EMA'] = ta.EMA(self.df['Adj Close'], timeperiod=10)
        return self.df['EMA']
    def RSI(self):
        self.df['RSI'] = ta.RSI(self.df['Adj Close'], timeperiod=14)
        return self.df['RSI']
