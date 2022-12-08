#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.ans = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0
        sum_left = self.dfs(node.left)
        sum_right = self.dfs(node.right)
        self.ans += abs(sum_left - sum_right)
        return sum_left + sum_right + node.val


# @lc code=end

