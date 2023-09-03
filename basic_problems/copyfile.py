# Write a program copyfile.py to copy one file to another. It should accept two 
# filenames as command-line arguments and copies the first one into the second

import sys

def copy_file(bda, destination):
    try:
        with open(bda, 'r') as source_file:
            content = source_file.read()

        with open(destination, 'w') as destination_file:
            destination_file.write(content)

        print(f"File '{bda}' copied to '{destination}'")
    except FileNotFoundError:
        print(f"Error: File '{bda}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python copyfile.py <source_filename> <destination_filename>")
    else:
        bda = sys.argv[1]
        destination = sys.argv[2]
        copy_file(bda, destination)

    # python copyfile.py source.txt destination.txt

