'''
Difficulty: Medium
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        j = 0
        res = 0
        dp = {'a': 0, 'b': 0, 'c': 0}

        for i in range(len(s)):
            dp[s[i]] += 1
        
            while all(v > 0 for v in dp.values()):
                dp[s[j]] -= 1
                j += 1
            res += j
        return res