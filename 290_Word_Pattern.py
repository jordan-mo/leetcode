'''
Difficulty: Easy
https://leetcode.com/problems/word-pattern/description/
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dp_p = {}
        dp_s = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if s[i] in dp_s and dp_s[s[i]] != pattern[i]:
                return False
            if pattern[i] in dp_p and dp_p[pattern[i]] != s[i]:
                return False

            dp_s[s[i]] = pattern[i]
            dp_p[pattern[i]] = s[i]
        return True