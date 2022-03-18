#
# @lc app=leetcode.cn id=654 lang=python3
#
# [654] 最大二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def dfs(nums: List[int]) -> TreeNode:

            if not nums: return None
            # 找出最大值，分出左右数组
            
            max_val = max(nums)
            max_index = nums.index(max_val)


            left = nums[:max_index]
            right = nums[max_index + 1:]

            root = TreeNode(max_val)

            root.left = dfs(left)
            root.right = dfs(right)
            return root

        return dfs(nums)

# @lc code=end

