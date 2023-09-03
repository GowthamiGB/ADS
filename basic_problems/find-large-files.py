# Write a program find-large-files.py to find files recursively in a directory tree that 
# are larger than given size. The program should accept the directory and the size as command-line argument. The size can be also be specified with K, M and G suffix for 
# KB, MB and GB respectively.

import sys
import os
import argparse

def convert_size_to_bytes(size_str):
    suffixes = {'K': 1024, 'M': 1024**2, 'G': 1024**3}
    if size_str[-1] in suffixes:
        return int(size_str[:-1]) * suffixes[size_str[-1]]
    return int(size_str)

def find_large_files(directory, min_size):
    try:
        min_size_bytes = convert_size_to_bytes(min_size)
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if file_size > min_size_bytes:
                    print(file_path)
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find large files in a directory.")
    parser.add_argument("directory", help="The directory to search in")
    parser.add_argument("min_size", help="Minimum size of files to find. Use K, M, or G suffix for KB, MB, or GB.", type=str)
    args = parser.parse_args()
    
    find_large_files(args.directory, args.min_size)

# python find-large-files.py /path/to/directory 1M

