#19. From a list containing ints, strings and floats, make three lists to store them separately

input_list = [2,3,4.5,'hello',2.5,2,'hey']

integers =[item for item in input_list if type(item) == int]
floating = [item for item in input_list if type(item) == float]
strings = [item for item in input_list if type(item) == str]

print(integers)
print(floating)
print(strings)