# LIST TRANSFORMER

import json

list = ['apple', 'banana', 'blueberry', 'pineapple', 'cranberry']
print(list)

# create functions that transform a list

def sort_list_ascend(list):
    result = sorted(list)
    return result

def sort_list_descend(list):
    result = sorted(list, reverse=True)
    return result

def list_to_dict(list):
    dictionary = {str(index): fruit for index, fruit in enumerate(list)}
    return dictionary

def list_to_json(list):
    dictionary = {str(index): fruit for index, fruit in enumerate(list)}
    json_data = json.dumps(dictionary, indent=2)
    return json_data

def list_to_str(list):
    string = ', '.join(list)
    return string


# store functions in a list

transformer = [
    sort_list_ascend,
    sort_list_descend,
    list_to_dict,
    list_to_json,
    list_to_str
]

# loop over list functions and store results

# for func in transformer:
#     result = func(list)
#     print(result)

# basic syntax: [EXPRESSION for ITEM in ITERABLE]
# create a list of squares with list comprehension
squares = [x**2 for x in range(10)]
# print(squares)

# create combined lists using multiple for loops
combinations = [(x, y) for x in ['chicken', 'beef', 'bison'] for y in ['barbeque', 'korean', 'smoked']]
# print(combinations)

# flattening a list of lists
nested_list = combinations
flattened = [item for sublist in nested_list for item in sublist]
# print(flattened)