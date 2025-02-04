'''
Difficulty: Easy
https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
'''

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res, tmp = 0, 0
        for i in range(len(nums)):
            if nums[i-1] >= nums[i]:
                tmp = 0
            tmp += nums[i]
            res = max(res, tmp)
        return res