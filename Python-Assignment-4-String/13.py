#13.Write a Python program to check whether a string starts with specified characters.

str = input('enter any string: ')
char = input('enter any specified character: ')

if str[0] == char:
  print('its correct')
else:
  print('its not a specified character..')