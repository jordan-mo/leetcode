'''
Difficulty: Medium
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
'''

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        a, b = float('inf'), float('-inf')
        res = 0
        for n in nums:
            a = min(n, a+n)
            b = max(n, b+n)
            res = max(res, abs(a), b)
        return res