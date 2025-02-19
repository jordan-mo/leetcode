'''
Difficulty: Medium
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
'''
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def dfs(s):
            if len(s) == n:
                heapq.heappush(res, s)
                return
            if len(res) == k:
                return
            for c in ['a','b', 'c']:
                if s != '' and s[-1] == c:
                    continue
                else:
                    s += c
                    dfs(s)
                    s = s[:len(s)-1]
        
        res = []
        dfs('')
        if len(res) <= k - 1:
            return ''
        ans = ''
        for _ in range(k):
            ans = heapq.heappop(res)
        return ans