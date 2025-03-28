'''
Difficulty: Easy
https://leetcode.com/problems/happy-number/description/
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n > 1:
            m, tmp = n, 0
            while m:
                cur = m % 10
                tmp += cur * cur
                m = m // 10
            if tmp in visited:
                break
            visited.add(tmp)
            n = tmp
        return n == 1