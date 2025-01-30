'''
Difficulty: Medium
https://leetcode.com/problems/simplify-path/description/
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        skip = set(['..', '.', '/', ''])
        for c in path:
            if c == '..' and stack:
                stack.pop()
            elif c not in skip:
                stack.append(c)
        res = ''
        for c in stack:
            res += '/' + c
        return res if res != '' else '/'