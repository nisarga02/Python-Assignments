#  11.Write a Python function to reverses a string if it's length is a multiple of 4

string = input('Enter any string: ')

if (len(string) % 4) == 0:
  print(string[::-1])
else:
  print(" it's length is not a multiple of 4")