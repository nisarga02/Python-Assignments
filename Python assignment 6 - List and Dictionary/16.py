# 16. Write a Python program to find the highest 3 values in a dictionary.

from heapq import nlargest

mydict = {'a': 300, 'b': 800, 'd': 400, 'c': 600, 'e': 500}

highest_values = nlargest(3, mydict.values())

print('first 3 highest values in dictionary',highest_values)