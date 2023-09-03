# Write a program head.py that takes a filename as command-line argument and prints the first 5 lines of it.

import sys

def head(bda, num_lines=5):
    try:
        with open(bda, 'r') as file:
            for _ in range(num_lines):
                line = file.readline()
                if not line:
                    break
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '{bda}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python head.py <bda>")
    else:
        bda = sys.argv[1]
        head(bda)

# python head.py filename.txt


