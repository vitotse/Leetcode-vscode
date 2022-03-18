#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    preTree = None

    def isValidBST(self, root: TreeNode) -> bool:

        if not root: return True
        
        left = self.isValidBST(root.left)


        if self.preTree and self.preTree.val >= root.val:

            return False

        self.preTree = root
        right = self.isValidBST(root.right)
        
        return left and right

# @lc code=end

