# 6.Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing' 
# Sample String : 'string'
# Expected Result : 'stringly'


def change_string_end(str):
  if len(str) < 3:
    print(str)
  elif str.endswith('ing') == True:
    print(str+'ly')
  else:
    print(str + 'ing')

change_string_end('string')
change_string_end('abc')
change_string_end('ab')