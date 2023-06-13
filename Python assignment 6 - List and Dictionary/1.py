#1. Write a Python script to sort (ascending and descending) a dictionary by value.

fruits = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3, 'elderberry': 1}

ascending_dict = dict(sorted(fruits.items(), key = lambda item: item[1]))
descending_dict = dict(sorted(fruits.items(), key = lambda item: item[1],reverse = True))

print("Ascending order: ",ascending_dict)
print("\nDescending order:",descending_dict)
