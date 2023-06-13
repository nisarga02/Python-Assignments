# 10. Write a Python program to remove a key from a dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print('dictionary before remove a key:',thisdict)

del thisdict['year']

print('\ndictionary after remove a key:',thisdict)