/*
 * @lc app=leetcode id=189 lang=swift
 *
 * [189] Rotate Array
 */

// @lc code=start
class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        
        if k == 0 {
            return
        }
        var i = k % nums.count

        var temp: [Int] = []

        while i > 0 {
            
            temp.insert(nums.popLast()!, at: 0)
            i -= 1
        }
        
        nums.insert(contentsOf: temp, at: 0)
        
    }
}
// @lc code=end

