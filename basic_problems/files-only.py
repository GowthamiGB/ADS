# Write a program files-only.py to find only file and not sub directories. Pass 
# directory name as command line argument.
# ask

import sys
import os

def list_files_only(ADS):
    try:
        files = [file for file in os.listdir(ADS) if os.path.isfile(os.path.join(ADS, file))]
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Error: Directory '{ADS}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python files-only.py <ADS>")
    else:
        ADS = sys.argv[1]
        list_files_only(ADS)

# python files-only.py /path/to/directory

