'''
Difficult:y: Easy
https://leetcode.com/problems/special-array-i/description/
'''

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        

        for i in range(1, len(nums)):
            if nums[i-1] % 2 == nums[i] % 2:
                return False
        return True