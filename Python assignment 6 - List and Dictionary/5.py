# 5. Write a Python program to iterate over dictionaries using for loops.
fruits = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3, 'elderberry': 1}
for keys,values in fruits.items():
  print(f'{keys}:{values}')