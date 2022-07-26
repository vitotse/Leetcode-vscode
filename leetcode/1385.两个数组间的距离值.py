#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#

# @lc code=start

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr2.sort()
        count = len(arr1)

        for i in range(0, len(arr1)):

            left, right = 0, len(arr2) - 1
            while left <= right:
                mid = (left + right) // 2

                # 检查是否符合距离
                if abs(arr2[mid] - arr1[i]) <= d:
                    count -= 1
                    break
                else:
                    # 二分法修改 arr2的索引
                    if arr1[i] - arr2[mid] < 0:
                        right = mid - 1
                    else:
                        left = mid + 1
        
        return count

# @lc code=end

