# 20. Write a Python program to extend a list without append.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

sample_data = [10, 20, 30]

result = [40, 50, 60] + sample_data

print('Result: ',result)