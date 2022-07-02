#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        carry = 0
        preNode = ListNode()

        curNode = preNode

        while l1 or l2 or carry > 0:

            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            curNode.next = ListNode((x + y + carry) % 10)
            curNode = curNode.next

            carry = (x + y + carry) // 10

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next

        return preNode.next


# @lc code=end

