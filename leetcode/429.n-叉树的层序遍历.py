#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        nodes, ans = [root], []
        while nodes:
            nxt, cur = [], []
            for node in nodes:
                cur.append(node.val)
                nxt += [child for child in node.children]
            nodes = nxt
            ans.append(cur)
        return ans

# @lc code=end

