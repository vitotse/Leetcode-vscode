/*
 * @lc app=leetcode.cn id=2 lang=swift
 *
 * [2] 两数相加
 *
 * https://leetcode-cn.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (33.68%)
 * Total Accepted:    116.7K
 * Total Submissions: 345.2K
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
 * 
 * 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
 * 
 * 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
 * 
 * 示例：
 * 
 * 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
 * 输出：7 -> 0 -> 8
 * 原因：342 + 465 = 807
 * 
 * 
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */


 public class ListNode {
      public var val: Int
      public var next: ListNode?
      public init(_ val: Int) {
          self.val = val
          self.next = nil
      }
}

class Solution {
    func addTwoNumbers(_ l1: ListNode?, _ l2: ListNode?) -> ListNode? {
        
        var result = ListNode(-1)
        
        var remainder = 0 // 余数
        var carry = 0 // 进位
        
        var node1:node1 = l1
        var node2: = l2
        
        while node1?.val != nil || node2?.val != nil || carry == 1 {
            
            remainder = (node1!.val + node2!.val + carry) % 10
            carry = (node1!.val + node2!.val + carry) / 10
            
            let next = ListNode(remainder)
            
            // 第一次
            if result.val == -1 {
                result = next
            }else {
                result.next = next
            }
            
            if l1!.next != nil {
                node1 = node1!.next
            }else{
                node1 = nil
            }
            
            if node2!.next != nil {
                node2 = node2!.next
            }else{
                node2 = nil
            }
            
        }
        
        return result
        
    }
}

