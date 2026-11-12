class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} #dictionary to store our pair of indices

        for i, nums in enumerate(nums):
            diff = target - nums
            if diff in dict:
                return [dict[diff], i]
            dict[nums] = i











