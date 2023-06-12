# 2. Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

def count_characters(string):
    char_frequency = {}

    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency

# Test the function
string = "google.com"
result = count_characters(string)
print(dict(sorted(result.items(), key=lambda x: x[1], reverse=True)))
