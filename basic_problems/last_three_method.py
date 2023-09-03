#  Write a function unique to find all the unique elements of a list
 
def unique(input_list):
    return list(set(input_list))

# Write a function dups to find all duplicates in the list.
def dups(input_list):
    unique_elements = set()
    duplicate_elements = []

    for element in input_list:
        if element in unique_elements:
            duplicate_elements.append(element)
        else:
            unique_elements.add(element)

    return duplicate_elements

# Write a function group(list, size) that take a list and splits into smaller lists of given size
def group(input_list, size):
    grouped_lists = [input_list[i:i + size] for i in range(0, len(input_list), size)]
    return grouped_lists



