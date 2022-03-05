#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: TreeNode, count: int):
        
        if root.left == None and root.right == None and count == 0:
            return True

        if root.left == None and root.right == None:
            return False

        if root.left != None:
            count -= root.left.val
            if self.dfs(root.left, count) == True:
                return True
            count += root.left.val

        if root.right != None:
            count -= root.right.val
            if self.dfs(root.right, count) == True:
                return True
            count += root.right.val

        return False


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        return self.dfs(root, targetSum-root.val)

# @lc code=end

