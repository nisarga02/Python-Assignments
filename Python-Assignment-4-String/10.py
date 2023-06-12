# 10.Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black,red, green, black
# Expected Result : black, green, red, white

def unique_sorted_words(words):
    word = words.split(",")
    unique_words = set(word)
    sorted_words = sorted(unique_words)
    print(", ".join(sorted_words))

sample_words = "red, white, black,red, green, black"
unique_sorted_words(sample_words)
