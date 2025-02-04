'''
Difficulty: Easy
https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/
'''

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        a1, a2 = [], []
        res = 0

        for n in nums:
            if a1 and a1[-1] <= n:
                a1 = []
            if a2 and a2[-1] >= n:
                a2 = []
            
            a1.append(n)
            a2.append(n)
            res = max(res, len(a1), len(a2))
        return res