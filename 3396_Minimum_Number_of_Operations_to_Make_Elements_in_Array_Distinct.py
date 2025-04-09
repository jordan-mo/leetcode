'''
Difficulty: Easy
https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/description/
'''

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        q = deque(nums)
        res = 0

        while q:
            if all(v <= 1 for v in count.values()):
                return res
            for _ in range(min(3, len(q))):
                count[q.popleft()] -= 1
            res += 1
        return res