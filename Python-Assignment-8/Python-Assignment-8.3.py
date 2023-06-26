def is_balanced_string(input_string):
    stack = []
    opening_delimiters = ['(', '[', '{']
    closing_delimiters = [')', ']', '}']
    delimiter_map = {closing: opening for closing, opening in zip(closing_delimiters, opening_delimiters)}

    for char in input_string:
        if char in opening_delimiters:
            stack.append(char)
        elif char in closing_delimiters:
            if not stack or stack[-1] != delimiter_map[char]:
                return False
            stack.pop()

    return len(stack) == 0

# Example usage:
input_string = "([{}])"
print(is_balanced_string(input_string))  # Output: True
