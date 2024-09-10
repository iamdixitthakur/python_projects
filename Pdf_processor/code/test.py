import glob 
import os

# Specify the directory path

directory = os.getcwd()

# Get all files in the directory
files = [os.path.basename(f) for f in glob.glob(f"{directory}/*")]
print(files)
