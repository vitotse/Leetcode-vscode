#
# @lc app=leetcode.cn id=1588 lang=python3
#
# [1588] 所有奇数长度子数组的和
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum = 0
        n = len(arr)
        for i, v in enumerate(arr):
            leftCount, rightCount = i, n - i - 1
            leftOdd = (leftCount + 1) // 2
            rightOdd = (rightCount + 1) // 2
            leftEven = leftCount // 2 + 1
            rightEven = rightCount // 2 + 1
            sum += v * (leftOdd * rightOdd + leftEven * rightEven)
        return sum 


# @lc code=end

