# 5.Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'


list =['abc','xyz']
char1 = list[0][0:2]
char2 = list[1][0:2]
str1 = char1+ list[1][2]
str2 = char2+ list[0][2]
print(str2, str1)
