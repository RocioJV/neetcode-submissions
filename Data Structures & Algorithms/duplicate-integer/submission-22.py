class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {}  # Dictionary to track seen numbers
        for i in nums:
            if i in prevMap: 
                return True 
            prevMap[i] = True 
        return False 
