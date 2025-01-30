'''
Difficulty: Easy
https://leetcode.com/problems/substring-matching-pattern/description/
'''

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        first, second = p.split('*')
        i, j = 0, 0
        if len(first) > 0:
            i = s.find(first)
            s = s[i+len(first):]
        if len(second) > 0:
            j = s.find(second)

        return i > -1 and j > -1