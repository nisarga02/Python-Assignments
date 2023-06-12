#7. Write a Python program that counts the number of elements within a list that are greater than 30.

list = [21,23,45,56,45,67,45,78,56,89,34,23,45,78,89,61,23]
count = 0

for num in list:
  if num > 30:
    count += 1

print(count)