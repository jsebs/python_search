import os

def search_string_text(directory, search_string):
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            with open(file_path) as file:
                for line_index, line in enumerate(file):
                    if search_string in line:
                        print(f"{search_string} was found in line {line_index + 1} of file -- {filename}")

directory = 'D:\\Dev\\Python\\test folder'
search_string = 'a b'
search_string_text(directory, search_string)