#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not (preorder and inorder):
            return None

        root = TreeNode(preorder[0])
        midIndex = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:midIndex+1],inorder[:midIndex])
        root.right = self.buildTree(preorder[midIndex+1:],inorder[midIndex+1:])
        return root

# @lc code=end

