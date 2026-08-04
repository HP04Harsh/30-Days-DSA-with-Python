class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        num_set = set(nums)
        min_val = min(nums)
        max_val = max(nums)
        
        # Iterate through the range and collect missing integers
        return [x for x in range(min_val, max_val + 1) if x not in num_set]