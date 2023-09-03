import sys
import os

def list_files(ADS):
    try:
        files = os.listdir(ADS)
        for file in files:
            if os.path.isfile(os.path.join(ADS, file)):
                print(file)
    except FileNotFoundError:
        print(f"Error: Directory '{ADS}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        current_directory = os.getcwd()
        list_files(current_directory)
    elif len(sys.argv) == 2:
        target_directory = sys.argv[1]
        list_files(target_directory)
    else:
        print("Usage: python ls.py [ADS]")
    # python ls.py
    # python ls.py /path/to/directory


