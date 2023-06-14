# 2) Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples: [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

input_data= [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_data = sorted(input_data, key = lambda item: item[1])

print('Sorted list: ',sorted_data)