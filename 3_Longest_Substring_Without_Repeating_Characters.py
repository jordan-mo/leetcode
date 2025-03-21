'''
Difficulty: Medium
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        i, j = 0, 0
        res = 0
        while i < len(s):
            count[s[i]] += 1
            while count[s[i]] > 1 and j < i:
                count[s[j]] -= 1
                j += 1
            res = max(res, i-j+1)
            i += 1
        return res