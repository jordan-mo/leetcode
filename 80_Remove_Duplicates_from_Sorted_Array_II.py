'''
Difficulty: Medium
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        count = Counter()

        while i < len(nums):
            count[nums[i]] += 1
            nums[i], nums[j] = nums[j], nums[i]
            
            i += 1
            j += 1
            if i < len(nums):
                count[nums[i]] += 1
                while i < len(nums) and count[nums[i]] > 3:
                    i += 1

        return j
            