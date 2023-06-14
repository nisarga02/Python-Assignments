# 2) Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
#    for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.


class ParenthesesValidator:
    def is_valid(self, s):
        stack = []
        brackets_map = {"(": ")", "{": "}", "[": "]"}
        
        for char in s:
            if char in brackets_map:
                stack.append(char)
            elif not stack or char != brackets_map[stack.pop()]:
                return False
        
        return not stack


validator =  ParenthesesValidator()
print(validator.is_valid("()"))
print(validator.is_valid("()[]{}"))
print(validator.is_valid( "[)"))
print(validator.is_valid("({[)]"))
print(validator.is_valid("{{{"))