/*
 * @lc app=leetcode.cn id=344 lang=swift
 *
 * [344] 反转字符串
 */

// @lc code=start
class Solution {
    func reverseString(_ s: inout [Character]) {
       for (index,char) in s.reversed().enumerated() {
           s[index] = char
       }


    }

    func reverseString(_ s: inout [Character]) {
       var head: Character?
        var tail: Character?
        
        
        for index in 0...s.count/2 - 1 {

            head = s[index]
            tail = s[s.count - index - 1]
            
            let temp: Character = tail!
            s[s.count - index - 1] = head!
            s[index] = temp
                        
       }


    }
        
}
// @lc code=end

