/*
 * @lc app=leetcode id=15 lang=swift
 *
 * [15] 3Sum
 */

// @lc code=start
class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        
        if nums.count < 3 {
            return []
        }

        var results:[[Int]] = []

        var header = nums[0]
        var center = nums[1]
        var tail = nums[2]

        var isZero = (header + center + tail) == 0 ? true : false

        if isZero {

            results.append([header,center,tail])
        }

        return results

    }
}
// @lc code=end

