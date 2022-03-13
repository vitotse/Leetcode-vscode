#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        def compareTree(tree1: TreeNode, tree2: TreeNode) -> bool:
            if not tree1 and tree2:
                return False
            elif tree1 and not tree2:
                return False
            elif not tree1 and not tree2:
                return True
            elif tree1.val != tree2.val:
                return False

            compareLeft = compareTree(tree1.left, tree2.left)
            compareRight = compareTree(tree1.right, tree2.right)

            return compareLeft and compareRight

        return compareTree(p, q)
        
# @lc code=end

