
# 16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
input_list = []

while True:
  item = input('Enter any items: ')
  if item == '':
    break
  input_list.append(item)

print('Input list:',input_list)

search_item = input('Enter an item to search and delete:')
for i in input_list:
  if i == search_item:
    input_list.remove(i)

print('Updated List:', input_list)

