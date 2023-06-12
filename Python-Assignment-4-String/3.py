# 3.Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
# Sample String : 'thisisniceone'
# Expected Result : 'thne”'
# Sample String : 'ab'
# Expected Result : 'abab'
# Sample String : 'f'
# Expected Result : Empty String


def get_string_char(str):
  string_length = len(str)
  if string_length == 2:
    print(str+str)
  elif string_length == 1:
    print("Empty string")
  else:
    print(str[:2]+str[-2:])

get_string_char("thisisniceone")
get_string_char("ab")
get_string_char("f")