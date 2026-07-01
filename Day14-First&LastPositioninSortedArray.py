from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # Helper function jo target ki sabse pehli insert position (low) batayega
        def findFirstIndex(val):
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < val:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        # Step 1: Target ki pehli position dhoondo
        start = findFirstIndex(target)
        
        # Step 2: Check karo ki target array mein sach me hai ya nahi
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
            
        # Step 3: Target se ek bade element (target + 1) ki position dhoondo
        # Woh index hamesha hamare target ke theek baad wala hoga
        end = findFirstIndex(target + 1) - 1
        
        return [start, end]