'''
15.Write a Python program to count repeated characters in a string.
Sample string: 'thequickbrownfoxjumpsoverthelazydog'
Expected output :
o 4
e 3
u 2
h 2
r 2
t 2
'''

def count_characters(string):
    char_count = {}
    repeated_chars = []

    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        if count > 1:
            repeated_chars.append((char, count))

    repeated_chars.sort(key=lambda x: (-x[1], x[0]))

    return repeated_chars

sample_string = 'thequickbrownfoxjumpsoverthelazydog'
repeated_chars = count_characters(sample_string)

for char, count in repeated_chars:
    print(char, count) 
