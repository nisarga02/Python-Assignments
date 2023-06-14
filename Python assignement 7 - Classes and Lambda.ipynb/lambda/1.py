
#Lambda
# 1) Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and print the result.
#  Sample Output: 25 48

num = int(input('Enter a number: '))
a = lambda a:a +15
x = lambda x,y:x * y
print(a(num), x(num,3))
