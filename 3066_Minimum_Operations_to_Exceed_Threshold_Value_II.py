'''
Difficulty: Medium
https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/?
'''

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = 0
        while len(nums) >= 2:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            if x >= k and y >= k:
                return res
            res += 1
            heapq.heappush(nums, min(x, y)*2 + max(x, y))
        return res