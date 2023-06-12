# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

class_held = int(input('Enter the number of classes held: '))
class_attended = int(input('Enter the number of classes attended: '))

percentage = (class_attended/class_held)*100
print(percentage)
if percentage > 75:
  print('Student is allowed to sit in exam')
else:
  print('Student is not allowed to sit in exam')
