'''
Difficulty: Medium
https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/
'''
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)

        prefixSum = sum(chalk)
        k %= prefixSum
        for j in range(n):
            k -= chalk[j]
            if k < 0:
                return j