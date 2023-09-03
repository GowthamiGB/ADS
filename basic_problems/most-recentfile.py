# Write a program most-recent-file.py to find the most recently modified file in the 
# given directory. The program should accept the directory name as command-line 
# argument and print path to the file (not just filename) that is most recently modified file.
# ask

import sys
import os

def find_most_recent_file(ADS):
    try:
        most_recent_file = None
        max_mtime = 0

        for root, _, files in os.walk(ADS):
            for file in files:
                file_path = os.path.join(root, file)
                file_mtime = os.path.getmtime(file_path)
                if file_mtime > max_mtime:
                    max_mtime = file_mtime
                    most_recent_file = file_path

        if most_recent_file:
            print(f"Most recently modified file: {most_recent_file}")
        else:
            print(f"No files found in '{ADS}'")
    except FileNotFoundError:
        print(f"Error: Directory '{ADS}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python most-recent-file.py <directory>")
    else:
        ADS = sys.argv[1]
        find_most_recent_file(ADS)

# python most-recent-file.py /path/to/directory


