#16. Write a Python program to print the index of the character in a string.

my_str = input('Enter a string: ')

for char in my_str:
  print(f"('{char}', {list.index(char)})")