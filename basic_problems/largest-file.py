# Write a program largest-file.py to find the largest file in the given directory. The 
# program should accept the directory name as command-line argument and print path 
# to the file (not just filename).
# ask

import sys
import os

def find_largest_file(ADS):
    try:
        largest_file = None
        max_size = 0

        for root, _, files in os.walk(ADS):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if file_size > max_size:
                    max_size = file_size
                    largest_file = file_path

        if largest_file:
            print(f"Largest file: {ADS}")
        else:
            print(f"No files found in '{ADS}'")
    except FileNotFoundError:
        print(f"Error: Directory '{ADS}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python largest-file.py <ADS>")
    else:
        ADS = sys.argv[1]
        find_largest_file(ADS)

# python largest-file.py /path/to/directory

