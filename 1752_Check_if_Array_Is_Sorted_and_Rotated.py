'''
Difficulty: Easy
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
'''

class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        n = len(nums)
        for i in range(n):
            isTrue = True
            for j in range(n):
                if nums[(i+j)%n] != arr[j]:
                    isTrue = False
                    break
            if isTrue:
                return True
        return False