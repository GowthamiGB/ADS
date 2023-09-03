# Write a program grep.py that takes a pattern and a filename as command-line 
# argument and prints all the lines in the file that contain given pattern.

import sys
import re

def grep(pattern, bda):
    try:
        with open(bda, 'r') as file:
            for line in file:
                if re.search(pattern, line):
                    print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '{bda}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <filename>")
    else:
        pattern = sys.argv[1]
        bda = sys.argv[2]
        grep(pattern, bda)

# python grep.py pattern filename.txt

