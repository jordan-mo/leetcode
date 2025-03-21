'''
Difficulty: Easy
https://leetcode.com/problems/divide-array-into-equal-pairs/description/
'''

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for k, v in count.items():
            if v % 2 != 0:
                return False
        return True