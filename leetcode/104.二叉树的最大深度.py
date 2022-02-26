#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def dfs(self, root: Optional[TreeNode], temp: int, ans: int):
        if not root:
            self.ans = max(self.ans, temp)
            return

        temp += 1
        self.dfs(root.left, temp, ans)
        self.dfs(root.right, temp, ans)
        return

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        temp = 0

        self.dfs(root, temp, self.ans)
        return self.ans 
# @lc code=end

