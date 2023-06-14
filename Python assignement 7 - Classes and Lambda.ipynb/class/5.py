# 5) Write a Python class to find the three elements that sum to zero from a set of n real numbers. Input array : [-25, -10, -7, -3, 2, 4, 8, 10] Output : [[-10, 2, 8], [-7, -3, 10]]

class ThreeSum:

  def find_three_sum(self,input_array):
    result = []
    for i in range(len(input_array)):
      for j in range(i+1,len(input_array)):
        for k in range(j+1,len(input_array)):
          if input_array[i] + input_array[j] + input_array[k] == 0:
            result.append([input_array[i], input_array[j], input_array[k]])
    return result

input_array = [-25, -10, -7, -3, 2, 4, 8, 10]     
three_sum = ThreeSum()
print(three_sum.find_three_sum(input_array))

