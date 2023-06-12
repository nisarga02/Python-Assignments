# 15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.
count = 0
total = 0
product = 1
num =1
average= 0

while(num!=0):
  inp = input('Enter q to quit: ')
  if inp == 'q':
    break
  num = int(input('Enter a number: '))
  total = total + num
  product = product * num
  count +=1

try:
  average = (total/count)

except ZeroDivisionError:
  print('enter any non-zero integer')

print(average)
print(product)
