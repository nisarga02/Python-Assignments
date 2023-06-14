# 8) Write a python class which has 2 methods get_string and print_string. get_string takes a string from the user and print_string prints the string in reverse order

class StringManipulator:
    def get_string(self):
        string = input('Enter a string: ')
        return string

    def print_string(self, string):
        return string[::-1]

manipulator = StringManipulator()
input_string = manipulator.get_string()
reversed_string = manipulator.print_string(input_string)
print(reversed_string)
