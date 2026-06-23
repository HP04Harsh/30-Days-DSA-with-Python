class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Map Roman numerals to integers
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # 2. Loop through the string
        for i in range(n):
            current_val = roman_map[s[i]]
            
            # 3. If a smaller value precedes a larger value, subtract it
            if i < n - 1 and current_val < roman_map[s[i + 1]]:
                total -= current_val
            else:
                total += current_val
                
        return total
