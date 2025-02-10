'''
Difficulty: Easy
https://leetcode.com/problems/clear-digits/description/?envType=daily-question&envId=2025-02-10
'''

class Solution:
    def clearDigits(self, s: str) -> str:
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        stack = []
        
        for c in s:
            if c in digits and stack:
                stack.pop()
            else:
                stack.append(c)
        
        return ''.join(stack)