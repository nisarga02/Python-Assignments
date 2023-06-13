# 13. Write a Python program to remove duplicates from Dictionary.

test_dict = {'a': 10,'a': 10, 'b': 25, 'b': 25, 'b': 25, 'c': 20, 'd': 10, 'e': 20}

new_dict = {}

for key in test_dict.keys():
  if key in new_dict.keys():
    continue
  else:
    new_dict[key] = test_dict[key]

print('dictionary after removing the duplicates',new_dict)