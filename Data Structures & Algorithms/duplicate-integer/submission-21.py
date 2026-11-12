class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {}  # Dictionary to track seen numbers
        for i in nums:
            if i in prevMap:  # Check if current number is already in the dictionary
                return True   # Duplicate found
            prevMap[i] = True  # Mark the number as seen
        return False  # No duplicates found
