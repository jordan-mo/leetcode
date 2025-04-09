'''
Difficulty: Medium
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers)-1

        while i < j:
            a, b = numbers[i], numbers[j]
            if a + b == target:
                return [i+1, j+1]
            
            if a + b > target:
                j -= 1
            else:
                i += 1