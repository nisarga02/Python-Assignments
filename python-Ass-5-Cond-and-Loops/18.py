# 18. From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
multiple_of_4 = [num for num in  input_list if num % 4 ==0]
multiple_of_6 = [num for num in  input_list if num % 6 ==0]
multiple_of_8 = [num for num in  input_list if num % 8 ==0]
multiple_of_10 = [num for num in  input_list if num % 10 ==0]
multiple_of_3 = [num for num in  input_list if num % 3 ==0]
multiple_of_5 = [num for num in  input_list if num % 5 ==0]
multiple_of_7 = [num for num in  input_list if num % 7 ==0]
multiple_of_9 = [num for num in  input_list if num % 9 ==0]

print(multiple_of_3)
print(multiple_of_4)
print(multiple_of_5)
print(multiple_of_6)
print(multiple_of_7)
print(multiple_of_8)
print(multiple_of_9)
print(multiple_of_10)
 