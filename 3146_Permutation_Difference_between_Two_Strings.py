'''
Difficulty: Easy
https://leetcode.com/problems/permutation-difference-between-two-strings/description/
'''
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        dp = {}
        res = 0

        for i in range(len(s)):
            dp[s[i]] = i
        
        for j in range(len(t)):
            res += abs(j - dp[t[j]])
        
        return res