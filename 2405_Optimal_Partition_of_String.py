'''
Difficulty: Medium
https://leetcode.com/problems/optimal-partition-of-string/description/
'''

class Solution:
    def partitionString(self, s: str) -> int:
        tmp = set()
        res = 1
        for c in s:
            if c in tmp:
                tmp = set()
                res += 1
            tmp.add(c)
        return res