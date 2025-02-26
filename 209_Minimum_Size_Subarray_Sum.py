'''
Difficulty: Medium
https://leetcode.com/problems/minimum-size-subarray-sum/description/
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        tmp = 0
        res = float('inf')
        j = 0
        for i in range(len(nums)):
            tmp += nums[i]
            while tmp-nums[j] >= target and j <= i:
                tmp -= nums[j]
                j += 1
            if tmp >= target:
                res = min(res, i-j+1)
        return res if res < float('inf') else 0