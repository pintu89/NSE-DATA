import pandas as pd


class Read_xlsx_File:
    '''
    A class for reading Excel (.xlsx) files using pandas library.

    Attributes:
        None

    Methods:
        Read_xlsx_File(file_path, sheet_name=None): 
            Reads an Excel file (.xlsx) from the specified file path.
            
            Args:
                file_path (str): The path to the Excel file.
                sheet_name (str, int, list, or None, optional): 
                    The name of the sheet to read. If None, reads all sheets and concatenates them.
                    Defaults to None.
            
            Returns:
                DataFrame: A pandas DataFrame containing the data read from the Excel file.
                None: If an error occurs during reading, returns None and prints the error message.

    '''
    def Read_xlsx_File(file_path, sheet_name=None):
        try:
            if sheet_name:
                data = pd.read_excel(file_path, sheet_name)

            elif sheet_name is None:
                return pd.concat(pd.read_excel(file_path, sheet_name=None), ignore_index=True)

            else:
                data = pd.read_excel(file_path)

            return data

        except Exception as e:
            print(f"Error reading Excel file:{e}")        
            return None
    def symbols(data):
        if data is not None:
            stock_list = data['SYMBOL \n'] + '.NS'
            Stock_List = stock_list.tolist()
            return Stock_List

'''            
Example:
file_path = "../../data/sym_data/NIFTY.xlsx"
sheet_name = int(input("0 = NFITY50\n1 = NIFTY100\n2 = NFITY200\n3 = NIFTY-NEXT50\n4 = Please inter your symbols in Port_folio1 and numbers are continues.5 6 7\n Please enter your Choice: "))  # Optional, provide the sheet name if needed
data = read_excel_file(file_path, sheet_name) 
'''