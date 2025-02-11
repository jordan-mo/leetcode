'''
Difficulty: Medium
https://leetcode.com/problems/remove-all-occurrences-of-a-substring/description/
'''

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        stack = ''

        for c in s:
            stack += c
            while len(stack) >= n and stack[-n:] == part:
                stack = stack[:len(stack)-n]
        return stack