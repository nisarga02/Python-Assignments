# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

sum = 0
avg = 0
count = 0
num =1

while num!=0:
  num = int(input(''))
  sum = sum + num
  count+=1 

average = (sum /count)

print(f'sum of {count} integer number is:{sum}')
print(f'sum of {count} integer number is:{average}')