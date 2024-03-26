import Read_file as rf
from Dn_dt import yf_dn as dn
from Write_dt import DataDownloader
import sys
sys.path.append('../Confi_file')
import Tech_Indi as td
from Signals import *
from Chart import *
from My_Wealth import *
# For Read Symbols from our Sym_data directory NIFTY files.
Rdata = input("1: NIFTY_50,\n2: NIFTY_100,\n3: NIFTY_200,\n4: NIFTY_N_50,\n0: Exit,\nEnter your choice: ")
if Rdata in['1','2','3','4','5']:
    Rfile = "../Data_File/sym_data/NIFTY.xlsx"
    Rdata = int(Rdata)-1
else:
    print("No Rdata type specified. Skipping Reading Symbols.")
    sys.exit()
symbols = rf.Read_xlsx_File.Read_xlsx_File(Rfile, Rdata)
symbols = rf.Read_xlsx_File.symbols(symbols)
H5data = dn.yf_data(symbols, symbols)





# For Download Data From Yfinance site.
D_data = input("1: Historical_data,\n2: 5min_data,\n3: ap_data,\n4: balance_sheet,\n0: Exit,\nEnter your choice: ")
if D_data == '1':
    D_file = "../Data_File/hisdata/hdata/hdata/"
    downloader = DataDownloader.download_historical_data
elif D_data == '2':
    downloader = DataDownloader.download_5min_data
    D_file = "../Data_File/hisdata/5Min_data/"
elif D_data == '3':
    downloader = DataDownloader.download_ap_data
    D_file = "../Data_File/hisdata/Recumdentions/"
elif D_data =='4':
    downloader = DataDownloader.balance_sheet
    D_file = "../Data_File/hisdata/bhavcopy/"
else:
    print("No D_data type specified. Skipping Downloading Data.")
    pass
if D_data:
    downloader = DataDownloader(D_file, symbols=symbols)
    downloader.download_and_save_data(D_data)
else:
    print("No data type specified. Skipping download.")
