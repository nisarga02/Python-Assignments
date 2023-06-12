'''
14. Write a Python program to print the following floating numbers upto 2 decimal places.
3.1415926
'''

number = float(input('Enter any number: '))
float_num = "{:.2f}".format(number)
print(float_num)