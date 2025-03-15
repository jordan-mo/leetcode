'''
Difficulty: Easy
https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description/
'''
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg, pos = 0, 0
        for n in nums:
            neg = neg + 1 if n < 0 else neg
            pos = pos + 1 if n > 0 else pos
        return max(neg, pos)