#12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

string = input('enter any string: ')

if string[0:2].isupper() == True:
  print(string.upper())
else:
  print('input is incorrect')
