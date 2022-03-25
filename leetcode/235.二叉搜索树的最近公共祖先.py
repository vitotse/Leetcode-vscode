#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def traversalCommonAncestor(cur: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
            if not cur: return cur

            if cur.val > p.val and cur.val > q.val:
                left = traversalCommonAncestor(cur.left, p, q)
                
                if left: return left

            if cur.val < p.val and cur.val < q.val:
                right = traversalCommonAncestor(cur.right, p, q)
                
                if right: return right

            return cur

        return traversalCommonAncestor(root, p, q)
        
# @lc code=end

