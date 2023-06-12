# 7.Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'


def first_apperance(str):
  if "not that poor" in str:
    str= str.replace('not that poor','good')
  print(str)

first_apperance('The lyrics is not that poor!')
first_apperance('The lyrics is poor!')