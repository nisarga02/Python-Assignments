# 3) Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

class SubsetGenerator:
    def get_unique_subsets(self, nums):
        subsets = [[]]
        for num in nums:
            subsets += [subset + [num] for subset in subsets]
        return subsets

nums = [4,5,6]

generator = SubsetGenerator()
print(generator.get_unique_subsets(nums))