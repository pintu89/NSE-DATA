import yfinance as yf
import pandas as pd
import datetime as dt


class yf_dn:
    def __init__(self, ticker):
        self.ticker = ticker

    def yf_ap_data(self, symbol):
        ap_data = yf.Ticker(symbol).recommendations
        return ap_data

    def yf_h_data(self, symbol, st_date=None, en_date=None, period=None):
        if period is None:
            period = 'max'
        h_data = yf.Ticker(symbol).history(start=st_date, end=en_date, period=period)
        return h_data
        
    def yf_data(self, symbol, st_date=None, en_date=None, period=None):
        if st_date is None:
            st_date = dt.datetime.now() - dt.timedelta(days=59)
        if st_date is None:
            en_date = dt.datetime.now()
            period = "max"
        h_data = yf.download(symbol, start=st_date, end=en_date, period=period, interval='5m', prepost=False)
        return h_data
    def yf_bl_data(self, symbol):
        """
        This function retrieves the balance sheet of a company from Yahoo Finance.

        Parameters:
        symbol (str): the ticker symbol of the company

        Returns:
        pandas.DataFrame: the balance sheet data of the company

        """
        st_dt = (dt.datetime.today() - dt.timedelta(days=365*10)).strftime('%y-%m-%d')
        en_dt = dt.datetime.today().strftime('%y-%m-%d')
        bl_data = yf.Ticker(symbol).balance_sheet
        return bl_data
    
'''
tickers=self.ticker
# Usage:
ticker = 'SBIN.NS'
yf_dn_obj = yf_dn(ticker)
SBIN_data = yf_dn_obj.yf_data(), yf_dn_obj.yf_h_data(), yf_dn_obj.yf_bl_data(), yf_dn_obj.yf_ap_data()
print(SBIN_data)
'''