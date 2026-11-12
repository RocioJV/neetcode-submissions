class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, nums in enumerate(nums):

            diff = target - nums
            if diff in num_dict:
                return [num_dict[diff], i]
            num_dict[nums] = i


