'''
Difficulty: Medium
https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/description/
'''

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        arr = defaultdict(list)

        for n in nums:
            cur = n
            tmp = 0
            while n > 0:
                tmp += n % 10
                n = n//10
            heapq.heappush(arr[tmp], cur*-1)
        res = -1
        for v in arr:
            if len(arr[v]) >= 2:
                res = max(res, heapq.heappop(arr[v])*-1 + heapq.heappop(arr[v])*-1)
        return res