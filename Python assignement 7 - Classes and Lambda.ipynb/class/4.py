# 4) Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number. Note: There will be one
#      solution for each input and do not use the same element twice. Input: numbers= [90, 20,10,40,50,60,70], target=50 Output: 3, 4

class Pair_finder:
    def find_pair(self, numbers, target):
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return i, j

target = 50
numbers = [90, 20, 10, 40, 50, 60, 70]

finder = Pair_finder()
pair_indices = finder.find_pair(numbers, target)
if pair_indices:
    print(f'{pair_indices[0]}, {pair_indices[1]}')
else:
    print("No pair found.")
