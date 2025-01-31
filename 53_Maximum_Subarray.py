'''
Difficulty: Medium
https://leetcode.com/problems/maximum-subarray/description/
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, tmp = float('-inf'), float('-inf')

        for n in nums:
            tmp = max(n, tmp + n)
            res = max(res, tmp)
        return res
    