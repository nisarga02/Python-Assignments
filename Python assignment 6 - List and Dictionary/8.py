# 8.  Write a Python program to sum all the items in a dictionary.

sample_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
sum_key = 0
sum_value = 0

for key,value in sample_dict.items():
  sum_key = sum_key +key
  sum_value = sum_value +value

print('The sum of all keys:',sum_key)
print('The sum of all values:',sum_value)
