#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            low, height = i + 1, n - 1

            while low <= height:

                mid = (low + height) // 2
                if numbers[mid] + numbers[i] == target:
                    return [i + 1, mid + 1]

                elif numbers[mid] + numbers[i] > target:
                    height = mid - 1
                else:
                    low = mid + 1


        return [-1, -1]


# @lc code=end

