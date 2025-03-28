'''
Difficulty: Medium
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        purchased = prices[0]

        for i in range(1, len(prices)):
            res += max(0, prices[i] - prices[i-1])
            
        return res