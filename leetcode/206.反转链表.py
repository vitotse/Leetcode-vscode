#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # 空链表或者只有一个节点的链表
        if head == None or head.next == None:
            return head

        p1 = head
        p2 = None

        while p1:
            temp = p1.next
            p1.next = p2
            p2 = p1
            p1 = temp
        return p2
        

# @lc code=end

