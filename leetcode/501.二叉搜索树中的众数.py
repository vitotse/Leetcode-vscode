#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        stack = []
        cur = root
        pre = None
        count, max_count = 0, 0
        res_list = []

        while cur or len(stack) > 0:
            if cur:
                stack.append(cur)
                cur = cur.left

            else:
                cur = stack.pop()
                if pre and pre.val == cur.val:
                    count += 1
                else:
                    count = 1

                if count == max_count:
                    res_list.append(cur.val)
                elif count > max_count:
                    res_list.clear()
                    res_list.append(cur.val)
                    max_count = count

                pre = cur
                cur = cur.right


        return res_list

# @lc code=end
