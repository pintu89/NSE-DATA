import pandas as pd
from Read_file import Read_xlsx_File
import datetime as dt
import Dn_dt as dn
import os
from tqdm import tqdm

class DataDownloader:
    def __init__(self, file_path, symbols):
        self.file_path = file_path
        self.data = Read_xlsx_File()
        self.stock_list = symbols
        self.yf_dn_obj = dn.yf_dn(self.stock_list)
        self.dir_ap = '../Data_File/hisdata/Recumdentions/'
        self.dirF = '../Data_File/hisdata/bhavcopy/'
        self.dir_h_data = '../Data_File/hisdata/hdata/'
        self.dir5 = '../Data_File/hisdata/5Min_data/'

    def download_and_save_data(self, data_type):
        if data_type == "1":
            self.download_historical_data()
        elif data_type == "2":
            self.download_5min_data()
        elif data_type == "3":
            self.download_ap_data()
        elif data_type == "4":
            self.download_balance_sheet()
        elif data_type == "0":
            pass
        else:
            self.download_5min_data()

    def download_ap_data(self):
        all_ap_data = {}
        for symbol in tqdm(self.stock_list, desc="downloading AP data", unit="stock"):
            data = self.yf_dn_obj.yf_ap_data(symbol=symbol)
            all_ap_data[symbol] = data
            file_name = os.path.join(self.dir_ap, f"{symbol}.xlsx")
            data.to_excel(file_name, index=True)
        print("All AP data saved.")

    def download_balance_sheet(self):
        all_F_data = {}
        for symbol in tqdm(self.stock_list, desc="downloading balance sheet data", unit="stock"):
            data = self.yf_dn_obj.yf_bl_data(symbol=symbol)
            all_F_data[symbol] = data
            data.to_excel(file_name, index=True)
            file_name = os.path.join(self.dirF, f"{symbol}.xlsx")
        print("All balance sheet data saved.")

    def download_historical_data(self):
        all_h_data = {}
        for symbol in tqdm(self.stock_list, desc="downloading historical data", unit="stock"):
            data = self.yf_dn_obj.yf_h_data(symbol=symbol)
            all_h_data[symbol] = data
            data.index = data.index.tz_localize(None)
            file_name = os.path.join(self.dir_h_data, f"{symbol}.xlsx")
            data.to_excel(file_name, index=True)
        print("All historical data saved.")

    def download_5min_data(self):
        st_date = dt.datetime.now() - dt.timedelta(days=59)
        for symbol in tqdm(self.stock_list, desc="downloading 5-minute data", unit="stock"):
            data = self.yf_dn_obj.yf_data(symbol=symbol, st_date=st_date)
            if data is not None and not data.empty:
                file_name = os.path.join(self.dir5, f"{symbol}.xlsx")
                if os.path.isfile(file_name):
                    with pd.ExcelWriter(file_name, engine='openpyxl',mode='a') as writer:
                        for date, df in data.groupby(data.index.date):
                            df.index = df.index.tz_localize(None)
                            sheet_name = str(date)
                            try:
                                df.to_excel(writer, sheet_name=str(date), index=True)
                            except ValueError:
                                # If sheet with the same name already exists, modify the name
                                idx = 1
                                while True:
                                    new_sheet_name = f"{sheet_name}_{idx}"
                                    try:
                                        df.to_excel(writer, sheet_name=new_sheet_name, index=True)
                                        break
                                    except ValueError:
                                        idx += 1     
                else:
                    with pd.ExcelWriter(file_name) as writer:
                        for date, df in data.groupby(data.index.date):
                            df.index = df.index.tz_localize(None)
                            df.to_excel(writer, sheet_name=str(date), index=True)
        print("All 5-minute data saved.")

if __name__ == "__main__":
    file_path = "../Data_File/hisdata"
    symbols = symbols
    data_type = input("Enter data type to download (ap_data, balance_sheet, historical_data, 5min_data): ")
    downloader = DataDownloader(file_path,symbols=symbols)
    downloader.download_and_save_data(data_type)