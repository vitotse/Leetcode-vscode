#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    sum = 0

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root: TreeNode) -> TreeNode:

            if not root:
                return root
            # 从右子树开始遍历
            dfs(root.right)
            
            self.sum += root.val
            root.val = self.sum

            # 最后遍历左子树
            dfs(root.left)

            return root
            
        return dfs(root)

# @lc code=end

