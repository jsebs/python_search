import csv
import os

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
        print(f"{search_string} was not found in any of the files")


directory = r'D:\Dev\Python\test folder'
search_string = 'boop'
search_string_csv(directory, search_string)