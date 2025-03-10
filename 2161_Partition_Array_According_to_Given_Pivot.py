'''
Difficulty: Medium
https://leetcode.com/problems/partition-array-according-to-given-pivot/description/
'''

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        for i in range(n):
            if nums[i] < pivot:
                res[left] = nums[i]
                left += 1
        for j in range(n-1, -1, -1):
            if nums[j] > pivot:
                res[right] = nums[j]
                right -= 1
        while left <= right:
            res[left], res[right] = pivot, pivot
            left += 1
            right -= 1
        return res