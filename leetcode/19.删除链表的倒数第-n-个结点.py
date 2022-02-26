#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # p1指针先移动n
        p1 = head
        while n > 0:
            p1 = p1.next
            n -= 1

        p2 = head
        if p1 == None:
            return p2.next

        # 同速移动指针
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next

        # 删除节点
        p2.next = p2.next.next
        return head

# @lc code=end

