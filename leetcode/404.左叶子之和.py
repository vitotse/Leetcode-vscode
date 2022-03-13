#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        left_value = self.sumOfLeftLeaves(root.left)
        right_value = self.sumOfLeftLeaves(root.right)

        mid_value = 0
        # 左叶子没有左右子树
        if root.left and not root.left.left and not root.left.right:
            mid_value = root.left.val
        sum = mid_value + left_value + right_value
        return sum
# @lc code=end

