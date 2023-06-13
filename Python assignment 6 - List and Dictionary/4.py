# 4. Write a Python script to check if a given key already exists in a dictionary.
fruits = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3, 'elderberry': 1}
sample_key = 'banana'

for keys in fruits.keys():
  if keys == sample_key:
    print('key already exist') 