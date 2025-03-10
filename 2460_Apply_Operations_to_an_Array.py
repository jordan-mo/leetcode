'''
Difficulty: Easy
https://leetcode.com/problems/apply-operations-to-an-array/description/
'''

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i + 1
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if j < len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
        return nums