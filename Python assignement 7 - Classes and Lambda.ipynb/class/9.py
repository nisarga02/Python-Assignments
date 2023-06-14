# 9) Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.
import math 

class Circle:
  def find_area(self,r):
    return r**2
  
  def find_perimeter(self,r):
    return 2*math.pi*r

calculate = Circle()
print(calculate.find_area(2))
print(calculate.find_perimeter(2))
