# 13. Take 10 integers from keyboard using loop and print their average value on the screen.

count = 0
total = 0

for i in range(10):
  num = int(input('Enter a number: '))
  total = total + num
  count +=1

average = (total/count)

print(average)