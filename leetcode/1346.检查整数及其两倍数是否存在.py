#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        arr.sort()

        q = 0
        
        for p in range(len(arr)):
            while q < len(arr) and arr[p] * 2 > arr[q]:
                q += 1
            if q != len(arr) and p != q and arr[p] * 2 == arr[q]:
                return True

        q = len(arr) - 1

        for p in range(len(arr) - 1, -1, -1):
            while q > -1 and arr[p] * 2 < arr[q]:
                q -= 1
            if q != -1 and p != q and arr[p] * 2 == arr[q]:
                return True

        return False
# @lc code=end

