import zipfile
import os

working_directory = r'C:\Users\smorton-zeller\Documents\Integrations Docs\Missing File Search\Houston'    # points to the directory with files to be unzipped
os.chdir(working_directory)

for file in os.listdir(working_directory):      # gets list of files in directory
    if zipfile.is_zipfile(file):        # checks if file is a zip
        with zipfile.ZipFile(file) as item:         # treat the file as a zip
            item.extractall()       # extract it in the working directory