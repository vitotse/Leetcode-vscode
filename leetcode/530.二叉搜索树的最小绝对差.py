#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ans = float('inf')
    pre = None

    def getMinimumDifference(self, root: TreeNode) -> int:
        def dfs(tree: TreeNode):
            if not tree: return 

            dfs(tree.left)

            if self.pre:
                self.ans = min(self.ans, tree.val - self.pre.val)

            self.pre = tree

            dfs(tree.right)

        dfs(root)
        return self.ans


# class Solution:
#     def getMinimumDifference(self, root: TreeNode) -> int:
#         stack = []
#         cur = root
#         pre = None
#         result = float('inf')
#         # 先进性中序遍历
#         while cur or stack:
#             if cur:
#                 stack.append(cur)
#                 cur = cur.left
#             else:
#                 cur = stack.pop()
#                 if pre:
#                     result = min(result, cur.val - pre.val) 
#                 pre = cur
#                 cur = cur.right

#         return result

# @lc code=end

