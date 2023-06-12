#20. Write a Python program to remove all consecutive duplicates of a given string.

def remove_consecutive_duplicates(string):
  previous = ''
  result = ''

  for char in string:
    if char != previous:
      result += char
      previous = char
  return result

remove_consecutive_duplicates('nisssargaaa')