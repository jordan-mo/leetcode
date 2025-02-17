'''
Difficulty: Medium
https://leetcode.com/problems/letter-tile-possibilities/description
'''

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def dfs(tmp):
            res = 0
            for k, v in count.items():
                if v > 0:
                    tmp += k
                    count[k] -= 1
                    res += 1 + dfs(tmp)
                    count[k] += 1
                    tmp = tmp[:len(tmp)-1]   
            return res
        return dfs('')