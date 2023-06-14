# 7) Write a Python class to reverse a string word by word.
# Input string : 'hello .py' Expected Output : '.py hello'

class ReversingString:
  def reverse_string(self,input_string):
    return ' '.join(input_string.split()[::-1])

reverse = ReversingString()
print(reverse.reverse_string('hello .py'))