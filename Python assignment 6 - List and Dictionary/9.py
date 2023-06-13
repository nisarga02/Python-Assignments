# 9. Write a Python program to multiply all the items in a dictionary.
sample_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
prod_key = 1
prod_value = 1

for key,value in sample_dict.items():
  prod_key = prod_key * key
  prod_value = prod_value * value

print('The product of all keys:',prod_key)
print('The product of all values:',prod_value)