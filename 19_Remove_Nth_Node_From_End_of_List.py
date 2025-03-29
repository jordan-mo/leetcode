'''
Difficulty: Medium
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        i, dp = 0, {}
        cur = head
        while cur:
            dp[i] = cur
            cur = cur.next
            i += 1
        #print(i-n-1, i-n+1)
        if i - n - 1 < 0:
            return head.next
        dp[i-n-1].next = dp[i-n+1] if i - n + 1 < i else None
        return head

        