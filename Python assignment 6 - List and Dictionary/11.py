# 11. Write a Python program to sort a dictionary by key.
mydict =  {3: 9, 2: 4, 4: 16, 1: 1, 5: 25}
print('dictionary before sorting:',mydict)

sorted_dict = dict(sorted(mydict.items()))

print('\ndictionary after sorting:',sorted_dict)
