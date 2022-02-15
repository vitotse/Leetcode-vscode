/*
 * @lc app=leetcode.cn id=13 lang=swift
 *
 * [13] 罗马数字转整数
 * I V  1     5        
 * X L  10    50
 * C D  100   500
 * M    1000
 *
 *  I II III IV V VI VII VIII IX X
 */
class Solution {
    func romanToInt(_ s: String) -> Int {
        
        if s.isEmpty {
            return 0
        }

        let numDic = ["I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000]

        var num: Int = 0

        for str in s {

            print(str)

            num += numDic[String(str)]!

        }

        print("total:" + "\(num)")
        
        return num
    }

    // // 计算符号
    // func calSign(_ first: String, _ second: String) -> Int {

    //     if first == I && second == V || X

    //     if first == X && second == L || C

    //     if first == C && second == D || M


    //         second - first
    //     else {
    //         first + second
    //     }


    //     return
    // }
}

let solution = Solution()

solution.romanToInt("VII")


