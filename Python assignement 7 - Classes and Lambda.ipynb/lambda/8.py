# 8) Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda. Minimum length : 10 input string: PaceWisd0m o/p: valid string


has_upper = lambda string: any(char.isupper() for char in string)
has_lower = lambda string: any(char.islower() for char in string)
has_digit = lambda string: any(char.isdigit() for char in string)
has_min_length = lambda string: len(string) >= 10

string = 'PaceWisd0m'

if all(x(string) for x in [has_upper,has_lower,has_digit,has_min_length]):
  print('valid string')
else:
  print('invalid string')