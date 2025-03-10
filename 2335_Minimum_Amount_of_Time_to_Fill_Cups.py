'''
Difficulty: Easy
https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description/
'''

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap = []
        for i in range(len(amount)):
            if amount[i] > 0:
                heapq.heappush(heap, (-amount[i], i))
        res = 0
        while heap:
            t1 = heapq.heappop(heap)
            t2 = None
            if heap:
                t2 = heapq.heappop(heap)
            if t1[0] + 1 != 0:
                heapq.heappush(heap, (t1[0]+1, t1[1]))
            if t2:
                if t2[0] + 1 != 0:
                    heapq.heappush(heap, (t2[0]+1, t2[1]))
            print(heap)
            res += 1
        return res