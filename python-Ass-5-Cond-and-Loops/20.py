#20.You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

input_list = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
squared_list = []

for num in input_list:
  squared_list.append(num**2)

print('Squared_items:',squared_list)