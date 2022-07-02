#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val) # 如果当前节点为空，也就意味着val找到了合适的位置，此时创建节点直接返回。
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val) # 递归创建右子树
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val) # 递归创建左子树
        return root

# @lc code=end

