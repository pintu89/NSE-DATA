import Read_file as rf
from Write_dt import DataDownloader
#Read_file
data = rf.Read_xlsx_File.Read_xlsx_File("../Data_File/sym_data/NIFTY.xlsx", int(input("0 = NFITY50\n1 = NIFTY100\n2 = NFITY200\n3 = NIFTY-NEXT50\n4 = Please inter your symbols in Port_folio1 and numbers are continues.5 6 7\n Please enter your Choice: ")))
symbols = rf.Read_xlsx_File.symbols(data)
# Wite File
file_path = "../Data_File/hisdata"
symbols = symbols
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
for symbol in symbols:
    try:
        # Assuming the file names are in the format 'hisdata/symbol.xlsx'
        file = f"{file_path}/{symbol}.xlsx"
        Hdata = rf.Read_xlsx_File.Read_xlsx_File(file)
        # Do something with Hdata
        print(f"Data for {symbol} is read successfully.")
    except FileNotFoundError:
        pass
        #print(f"File for {symbol} not found.")