# Write a program wc.py that takes filename as argument and counts number of lines, words and chars in file.

import sys

def wc(bda):
    try:
        with open(bda, 'r') as file:
            content = file.read()
            lines = content.count('\n') + 1  # Counting lines by counting newline characters
            words = len(content.split())     # Counting words by splitting content into a list of words
            chars = len(content)             # Counting characters in the content

            print(f"Lines: {lines}")
            print(f"Words: {words}")
            print(f"Characters: {chars}")
    except FileNotFoundError:
        print(f"Error: File '{bda}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc.py <filename>")
    else:
        bda = sys.argv[1]
        wc(bda)

# python wc.py filename.txt
