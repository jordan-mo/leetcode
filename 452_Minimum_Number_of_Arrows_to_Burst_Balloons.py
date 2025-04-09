'''
Difficulty: Medium
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        res = 0
        dist = float('-inf')
        #print(points)
        for i, j in points:
            if i > dist:
                dist = j
                res += 1
        return res