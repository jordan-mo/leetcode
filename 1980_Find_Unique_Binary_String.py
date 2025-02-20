'''
Difficulty: Medium
https://leetcode.com/problems/find-unique-binary-string/description/
'''
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)
        def dfs(s):
            if len(s) == n and s not in nums:
                return s
            if len(s) >= n:
                return ''
            return dfs(s+'0') or dfs(s+'1')
        return dfs('')