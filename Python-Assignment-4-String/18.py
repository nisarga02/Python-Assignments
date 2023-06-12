# '''
# 18.Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
# '''

def swap_comma_and_dot(string):
  result = ''

  for char in string:
    if char == '.':
      result += ','
    elif char == ',':
      result += '.'
    else:
      result += char
  return result

swap_comma_and_dot('32.054,23')