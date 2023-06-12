#19. Write a Python program to find smallest and largest word in a given string.

input_string = 'abc ab a abcdeefgh abcd abcde abcdef abcdefg'

string = input_string.split()

max_word = string[0]
min_word = string[0]

for i in string:
    if len(i) > len(max_word):
      max_word = i
    elif len(i) < len(min_word):
      min_word = i


print('longets word:',max_word)
print('smallest word:',min_word)