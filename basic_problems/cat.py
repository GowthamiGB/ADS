#  Write a program cat.py that takes a filename as command-line argument and prints 
# all the contents of that file.

import sys

def cat(bda):
    try:
        with open(bda, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{bda}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cat.py <bda>")
    else:
        bda = sys.argv[1]
        cat(bda)

    # python cat.py filename.txt
