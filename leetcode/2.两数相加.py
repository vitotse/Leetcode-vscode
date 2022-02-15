#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        preNode = ListNode()

        curNode = preNode

        node1 = l1
        node2 = l2

        while (node1 != None or node2 != None):

            sum = node1.val + node2.val + carry

            carry = sum / 10
            curNode.next = ListNode(val=sum % 10)

            curNode = curNode.next
            node1 = node1.next
            node2 = node2.next
        
        if carry == 1:
            curNode.next = ListNode(val=1)

        return preNode.next


# @lc code=end

