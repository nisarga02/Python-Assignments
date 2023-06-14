
# 7) Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
# Original Matrix: [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
#  Original Matrix: [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# Sort the said matrix in ascending order according to the sum of its rows [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]

original_matrix = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
sorted_matrix = sorted(original_matrix, key = lambda x:sum(x))
print('Sorted matrix',sorted_matrix)
