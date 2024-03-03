import Read_file as rf
from Write_dt import DataDownloader
#Read_file
data = rf.Read_xlsx_File.Read_xlsx_File("../Data_File/sym_data/NIFTY.xlsx", int(input("0 = NFITY50\n1 = NIFTY100\n2 = NFITY200\n3 = NIFTY-NEXT50\n4 = Please inter your symbols in Port_folio1 and numbers are continues.5 6 7\n Please enter your Choice: ")))
symbols = rf.Read_xlsx_File.symbols(data)
# Wite File
file_path = "../Data_File/hisdata"
symbols = symbols
data_type = input("Enter data type to download (ap_data, balance_sheet, historical_data, 5min_data): ")

# Check if data_type is specified and not empty
if data_type:
    downloader = DataDownloader(file_path, symbols=symbols)
    downloader.download_and_save_data(data_type)
else:
    print("No data type specified. Skipping download.")

for symbol in symbols:
    try:
        # Assuming the file names are in the format 'hisdata/symbol.xlsx'
        file = f"{file_path}/{symbol}.xlsx"
        Hdata = rf.Read_xlsx_File.Read_xlsx_File(file)
        # Do something with Hdata
        print(f"Data for {symbol} is read successfully.")
    except FileNotFoundError:
        print(f"File for {symbol} not found.")