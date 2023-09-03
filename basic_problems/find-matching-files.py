# Write a program find-matching-files.py to find files recursively in a directory tree 
# matching given wildcard pattern. The program should accept the directory and the 
# pattern as command-line argument.

import sys
import os
import glob

def find_matching_files(ADS, pattern):
    try:
        matching_files = glob.glob(os.path.join(ADS, '**', pattern), recursive=True)
        for file_path in matching_files:
            print(file_path)
    except FileNotFoundError:
        print(f"Error: Directory '{ADS}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python find-matching-files.py <ADS> <pattern>")
    else:
        ADS = sys.argv[1]
        pattern = sys.argv[2]
        find_matching_files(ADS, pattern)
        
# python find-matching-files.py /path/to/directory *.txt
