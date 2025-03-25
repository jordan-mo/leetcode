'''
Difficulty: Medium
https://leetcode.com/problems/count-days-without-meetings/description/
'''

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        n = [meetings[0]]

        for i in range(1, len(meetings)):
            if meetings[i][0] <= n[-1][1]:
                n[-1][1] = max(n[-1][1], meetings[i][1])
            else:
                n.append(meetings[i])
        res = 0
        for i in range(1, len(n)):
            res += n[i][0] - n[i-1][1] - 1
        #print(n)
        #print(res)
        res += n[0][0] - 1
        res += days - n[-1][1] 
        #print(res)
        return res