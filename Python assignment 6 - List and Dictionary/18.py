# 18. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False


sample_list = [{},{},{}]

all_empty = all(len(dictionary) == 0 for dictionary in sample_list)

print(all_empty)