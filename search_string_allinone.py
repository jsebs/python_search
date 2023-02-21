# to install the proper libraries open the command prompt and enter the following command
# pip install wheel openpyxl xlrd pandas

import csv
import os
import pandas as pd

def search_string_csv(directory, search_string):
    found = False
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            with open(file_path) as csvfile:
                reader = csv.reader(csvfile)
                for row_index, row in enumerate(reader):
                    for cell_index, cell in enumerate(row):
                        if cell == search_string:
                            found = True
                            print(f"{search_string} was found in cell [{row_index}, {cell_index}] of file -- {filename}")
    if not found:
        print(f"{search_string} was not found in any of the .csv files")

def search_string_text(directory, search_string):
    found = False
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path) as file:
                for line_index, line in enumerate(file):
                    if search_string in line:
                        found = True
                        print(f"{search_string} was found in line {line_index + 1} of file -- {filename}")
    if not found:
        print(f"{search_string} was not found in any of the .txt files")

def search_string_xls(directory, search_string):
    found = False
    for filename in os.listdir(directory):
        if filename.endswith('.xls'):
            file_path = os.path.join(directory, filename)
            df = pd.read_excel(file_path, engine='xlrd')
            for row_index, row in df.iterrows():
                for col_index, cell in enumerate(row):
                    if str(cell).find(search_string) != -1:
                        found = True
                        print(f"{search_string} was found in cell [{row_index}, {col_index}] of file -- {filename}")
    if not found:
        print(f"{search_string} was not found in any of the .xls files")

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
        print(f"{search_string} was not found in any of the .xlsx files")


# directory is the variable where you specify the directory to be searched 
# search_string is the variable where you specify what you're looking for within the given directory 
# e.g. directory = r'D:\Dev\Python\test folder' - leave the character "r" before the first apostrophe in the file path as that converts the path into a raw string for ease of use
# e.g. search_string = 'jimmy@aol.com' - you should only be searching for one string/field at a time (last name, email address, etc.)
# leave both apostophes wrapping the file path and your search string
directory = r'D:\Dev\Python\test folder'
search_string = 'shark'

search_string_csv(directory, search_string)
search_string_text(directory, search_string)
search_string_xls(directory, search_string)
search_string_xlsx(directory, search_string)