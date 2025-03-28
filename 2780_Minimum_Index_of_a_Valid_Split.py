'''
Difficulty: Medium
https://leetcode.com/problems/minimum-index-of-a-valid-split/description/
'''

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        count = Counter(nums)
        dp = {}
        for i in range(n):
            cur = nums[i]
            dp[cur] = dp.get(cur, 0) + 1
            count[cur] -= 1
            if dp[cur] * 2 > i + 1 and count[cur] * 2 > n - 1 - i:
                return i
        return -1