'''
Difficulty: Medium
https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        def dfs(node):
            self.tree.add(node.val)
            if node.right:
                node.right.val = node.val*2 + 2
                dfs(node.right)
            if node.left:
                node.left.val = node.val * 2 + 1
                dfs(node.left)
        self.tree = set([0])
        root.val = 0
        dfs(root)

    def find(self, target: int) -> bool:
        return target in self.tree
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)