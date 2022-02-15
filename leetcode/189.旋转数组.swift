/*
 * @lc app=leetcode.cn id=189 lang=swift
 *
 * [189] 旋转数组
 */

// @lc code=start
class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {

        var array:[Int] = []
        
        
        if k > nums.count {
            k = nums.count%k
        }
        
        while k > 0 {
                        
            k -= 1
        }
        
        for index in 0..<k {
            
        }

        if let last = nums.last {
            
        }
    }
}
// @lc code=end

