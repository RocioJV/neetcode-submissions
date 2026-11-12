class Solution: # create a class called "solution"
# define twoSum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap
        num_dict = {}
# Iterate through the nums list, where i is the index and num is the value
        for i, nums in enumerate(nums):

            diff = target - nums
            if diff in num_dict:
                return [num_dict[diff], i]
            num_dict[nums] = i


