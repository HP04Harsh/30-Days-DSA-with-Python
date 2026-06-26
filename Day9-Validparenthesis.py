class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False 
                # else block hata diya kyunki pop pehle hi element delete kar chuka hai
            else:
                # Agar character opening bracket hai, tab stack me append karo
                stack.append(char)    
                
        return len(stack) == 0