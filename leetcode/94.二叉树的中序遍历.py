#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root: 
            return []

        ans = []

        def dfs(ans, root: TreeNode):

            if not root: 
                return

            dfs(ans, root.left)
            ans.append(root.val)
            dfs(ans, root.right)
        dfs(ans,root)

        return ans

    
# @lc code=end

