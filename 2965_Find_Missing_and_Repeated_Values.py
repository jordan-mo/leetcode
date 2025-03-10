'''
Difficulty: Easy
https://leetcode.com/problems/find-missing-and-repeated-values/description/
'''

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = {k: 0 for k in range(1, (n*n)+1)}
        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1
        
        ans = [-1, -1]
        for k, v in count.items():
            if v == 0:
                ans[1] = k
            if v == 2:
                ans[0] = k
        return ans