# 17. Using range(1,101), make three list, 
# one containing all even numbers
# one containing all odd numbers 
# One containing only prime numbers..

even_numbers = []
odd_numbers = []
prime_numbers = []

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(1, 101):
    if num % 2 == 0:
        even_numbers.append(num)
    elif num % 2 != 0:
        odd_numbers.append(num)
    if is_prime(num):
        prime_numbers.append(num)

print('Even numbers:', even_numbers)
print('Odd numbers:', odd_numbers)
print('Prime numbers:', prime_numbers)
