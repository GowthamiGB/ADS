# Write a program sumfile.py that takes a filename as argument and prints sum of all numbers in that file. 
# It is assumed that the file will only have one number in every line.


import sys

def sumfile(bda):
    try:
        total_sum = 0
        with open(bda, 'r') as file:
            for line in file:
                try:
                    number = float(line.strip())
                    total_sum += number
                except ValueError:
                    print(f"Warning: Skipping invalid number on line '{line.strip()}'")

        print(f"Sum of numbers in '{bda}': {total_sum}")
    except FileNotFoundError:
        print(f"Error: File '{bda}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sumfile.py <filename>")
    else:
        bda = sys.argv[1]
        sumfile(bda)
# python sumfile.py numbers.txt
