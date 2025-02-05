# helpers.py
import os
import glob
import json


def getOldValuesFromJson():

    # read json file into a dictionary
    
    # Define the file path
    file_path = r"C:\Users\Win 10 PC\Desktop\scripts\MxSim\mxStats\playTime.json"

    home_dir = os.path.expanduser("~")

    with open("C:\\Users\Win 10 PC\Desktop\scripts\MxSim\mxStats\playTime.json", "r") as f:
        data = json.load(f)
        return data
    
values = getOldValuesFromJson()
print(values['Times played total'])

def get_most_recent_lastlap_folder():
    # Get the path to the user's home directory
    home_dir = os.path.expanduser("~")

    # Construct the base path to the target directory
    base_path = os.path.join(home_dir, 'AppData', 'Local', 'MX Simulator')

    # Search for all lastlap.mxdemo files in subdirectories
    search_pattern = os.path.join(base_path, '**', 'lastlap.mxdemo')
    lastlap_files = glob.glob(search_pattern, recursive=True)

    if not lastlap_files:
        return None
    else:
        # Find the lastlap.mxdemo file with the most recent write time
        most_recent_file = max(lastlap_files, key=os.path.getmtime)

        # Get the directory of the most recent file
        most_recent_file_dir = os.path.dirname(most_recent_file)

        # Get the name of the directory
        most_recent_folder_name = os.path.basename(most_recent_file_dir)

        return most_recent_folder_name
    
