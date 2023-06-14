#  3) Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]

input_data = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
               {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
               {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sorted_data = sorted(input_data, key = lambda item: item['color'])

print('Sorted dict: ',sorted_data)
