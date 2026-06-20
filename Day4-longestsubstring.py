class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize an empty set to track unique characters
        char_set = set()
        
        # Left pointer and maximum length tracker
        left = 0
        max_len = 0

        # Move the right pointer through the string
        for right in range(len(s)):
            # If duplicate found, shrink window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add current character and update max length
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
            
        return max_len