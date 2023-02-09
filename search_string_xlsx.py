import pandas as pd #to install pandas -> command prompt -> pip install wheel -> pip install openpyxl -> pip install pandas
import os

def search_string_xlsx(directory, search_string):
    found = False
    for filename in os.listdir(directory):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(directory, filename)
            df = pd.read_excel(file_path, engine='openpyxl')
            for row_index, row in df.iterrows():
                for col_index, cell in enumerate(row):
                    if str(cell).find(search_string) != -1:
                        found = True
                        print(f"{search_string} was found in cell [{row_index}, {col_index}] of file -- {filename}")
    if not found:
        print(f"{search_string} was not found in any of the files")


directory = r'D:\Dev\Python\test folder'
search_string = 'boop'
search_string_xlsx(directory, search_string)