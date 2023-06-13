# 12. Write a Python program to get the maximum and minimum value in a dictionary.
mydict =  {3: 9, 2: 4, 4: 16, 1: 1, 5: 25}

max_value = max(mydict.values())
min_value = min(mydict.values())

print('Maximum value in a dictionary: ',max_value)
print('Minimum value in a dictionary: ',min_value)